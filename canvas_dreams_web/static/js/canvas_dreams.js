document.addEventListener('DOMContentLoaded', function() {
    // Canvas setup
    const canvas = document.getElementById('drawingCanvas');
    const ctx = canvas.getContext('2d');
    
    // Set canvas size
    function resizeCanvas() {
        const mainArea = document.querySelector('.main-area');
        canvas.width = mainArea.clientWidth;
        canvas.height = mainArea.clientHeight;
        
        // Fill with background color
        ctx.fillStyle = backgroundColor;
        ctx.fillRect(0, 0, canvas.width, canvas.height);
    }
    
    // Constants and variables
    const COLORS = [
        '#ff6961', // Coral
        '#ffb480', // Peach
        '#f8f38d', // Pale Yellow
        '#42d6a4', // Mint
        '#087e8b', // Teal
        '#5945a4', // Purple
        '#e94e77', // Pink
        '#ff914d', // Orange
        '#ff0000', // Red
        '#00ff00', // Green
        '#0000ff', // Blue
        '#ffff00'  // Yellow
    ];
    
    // Game state
    let currentColor = COLORS[Math.floor(Math.random() * COLORS.length)];
    let brushSize = 15;
    let particles = [];
    let mode = 'draw';
    let symmetry = 8;
    let backgroundColor = '#000000';
    let isDrawing = false;
    let showHelp = false;
    let lastX, lastY;
    
    // Initialize color palette
    const colorPalette = document.getElementById('colorPalette');
    COLORS.forEach(color => {
        const swatch = document.createElement('div');
        swatch.className = 'color-swatch';
        swatch.style.backgroundColor = color;
        if (color === currentColor) {
            swatch.classList.add('active');
        }
        swatch.addEventListener('click', () => {
            document.querySelectorAll('.color-swatch').forEach(s => s.classList.remove('active'));
            swatch.classList.add('active');
            currentColor = color;
        });
        colorPalette.appendChild(swatch);
    });
    
    // Particle class
    class Particle {
        constructor(x, y, color, size = 3, velocity = {x: 0, y: 0}, life = 100) {
            this.x = x;
            this.y = y;
            this.color = color;
            this.size = size;
            this.velocity = velocity;
            this.life = life;
            this.originalLife = life;
            this.gravity = mode === 'gravity' ? 0.1 : 0;
        }
        
        update() {
            this.x += this.velocity.x;
            this.y += this.velocity.y + this.gravity;
            this.life--;
            this.size = Math.max(1, this.size * (this.life / this.originalLife));
        }
        
        draw() {
            const alpha = this.life / this.originalLife;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fillStyle = this.color.replace('rgb', 'rgba').replace(')', `,${alpha})`);
            ctx.fill();
        }
    }
    
    // Drawing functions
    function createSymmetricPoints(x, y, numSymmetry = 8) {
        const points = [];
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const dx = x - centerX;
        const dy = y - centerY;
        const radius = Math.sqrt(dx*dx + dy*dy);
        
        if (radius < 5) return points;
        
        const angle = Math.atan2(dy, dx);
        
        for (let i = 0; i < numSymmetry; i++) {
            const newAngle = angle + (2 * Math.PI * i / numSymmetry);
            const newX = centerX + radius * Math.cos(newAngle);
            const newY = centerY + radius * Math.sin(newAngle);
            points.push({x: newX, y: newY});
        }
        
        return points;
    }
    
    function createParticles(x, y, count = 10) {
        for (let i = 0; i < count; i++) {
            const angle = Math.random() * Math.PI * 2;
            const speed = Math.random() * 1.5 + 0.5;
            const velocity = {
                x: Math.cos(angle) * speed,
                y: Math.sin(angle) * speed
            };
            const size = Math.random() * brushSize * 0.3 + brushSize * 0.2;
            const life = Math.random() * 70 + 30;
            
            // Create a slightly varied color
            const colorVariation = 20;
            const baseColor = hexToRgb(currentColor);
            const variedColor = `rgb(
                ${Math.max(0, Math.min(255, baseColor.r + (Math.random() * colorVariation * 2 - colorVariation)))},
                ${Math.max(0, Math.min(255, baseColor.g + (Math.random() * colorVariation * 2 - colorVariation)))},
                ${Math.max(0, Math.min(255, baseColor.b + (Math.random() * colorVariation * 2 - colorVariation)))}
            )`;
            
            particles.push(new Particle(x, y, variedColor, size, velocity, life));
        }
    }
    
    function hexToRgb(hex) {
        const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
        return result ? {
            r: parseInt(result[1], 16),
            g: parseInt(result[2], 16),
            b: parseInt(result[3], 16)
        } : {r: 0, g: 0, b: 0};
    }
    
    function draw(x, y) {
        if (mode === 'draw') {
            ctx.beginPath();
            ctx.arc(x, y, brushSize, 0, Math.PI * 2);
            ctx.fillStyle = currentColor;
            ctx.fill();
            
            // Connect lines when moving fast
            if (lastX && lastY) {
                ctx.beginPath();
                ctx.moveTo(lastX, lastY);
                ctx.lineTo(x, y);
                ctx.lineWidth = brushSize * 2;
                ctx.strokeStyle = currentColor;
                ctx.stroke();
            }
            
            lastX = x;
            lastY = y;
        } else if (mode === 'spray') {
            createParticles(x, y, 5);
        } else if (mode === 'kaleidoscope') {
            const points = createSymmetricPoints(x, y, symmetry);
            points.forEach(point => {
                ctx.beginPath();
                ctx.arc(point.x, point.y, brushSize, 0, Math.PI * 2);
                ctx.fillStyle = currentColor;
                ctx.fill();
                createParticles(point.x, point.y, 2);
            });
        } else if (mode === 'gravity') {
            for (let i = 0; i < 3; i++) {
                const angle = Math.random() * Math.PI / 2 - Math.PI / 4;
                const speed = Math.random() * 4 + 1;
                const velocity = {
                    x: Math.cos(angle) * speed,
                    y: -Math.sin(angle) * speed * 2
                };
                const size = Math.random() * brushSize * 0.4 + brushSize * 0.3;
                const life = Math.random() * 100 + 50;
                
                const baseColor = hexToRgb(currentColor);
                const variedColor = `rgb(
                    ${Math.max(0, Math.min(255, baseColor.r + (Math.random() * 40 - 20)))},
                    ${Math.max(0, Math.min(255, baseColor.g + (Math.random() * 40 - 20)))},
                    ${Math.max(0, Math.min(255, baseColor.b + (Math.random() * 40 - 20)))}
                )`;
                
                particles.push(new Particle(x, y, variedColor, size, velocity, life));
            }
        }
    }
    
    // Button actions
    function setMode(newMode) {
        mode = newMode;
        document.getElementById('currentMode').textContent = newMode.charAt(0).toUpperCase() + newMode.slice(1);
        
        // Update active button
        document.querySelectorAll('.mode-btn').forEach(btn => btn.classList.remove('active'));
        document.getElementById(`${newMode}Mode`).classList.add('active');
        
        // Show/hide symmetry controls based on mode
        document.getElementById('symmetrySection').style.opacity = mode === 'kaleidoscope' ? '1' : '0.5';
    }
    
    function clearCanvas() {
        ctx.fillStyle = backgroundColor;
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        particles = [];
    }
    
    function saveArtwork() {
        const link = document.createElement('a');
        link.download = `canvas_dreams_${Date.now()}.png`;
        link.href = canvas.toDataURL();
        link.click();
        
        const saveMessage = document.getElementById('saveMessage');
        saveMessage.textContent = 'Artwork saved!';
        setTimeout(() => {
            saveMessage.textContent = '';
        }, 3000);
    }
    
    function toggleBackground() {
        backgroundColor = backgroundColor === '#000000' ? '#ffffff' : '#000000';
        clearCanvas();
    }
    
    function toggleHelp() {
        document.getElementById('helpOverlay').classList.toggle('hidden');
    }
    
    // Event listeners
    canvas.addEventListener('mousedown', function(e) {
        if (e.button === 0) { // Left mouse button
            isDrawing = true;
            const rect = canvas.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            draw(x, y);
        } else if (e.button === 2) { // Right mouse button
            const randomIndex = Math.floor(Math.random() * COLORS.length);
            currentColor = COLORS[randomIndex];
            document.querySelectorAll('.color-swatch').forEach((swatch, index) => {
                swatch.classList.toggle('active', index === randomIndex);
            });
        }
    });
    
    canvas.addEventListener('mousemove', function(e) {
        if (isDrawing) {
            const rect = canvas.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            draw(x, y);
        }
    });
    
    canvas.addEventListener('mouseup', function() {
        isDrawing = false;
        lastX = null;
        lastY = null;
    });
    
    canvas.addEventListener('mouseleave', function() {
        isDrawing = false;
        lastX = null;
        lastY = null;
    });
    
    // Prevent context menu on right-click
    canvas.addEventListener('contextmenu', function(e) {
        e.preventDefault();
    });
    
    // Button event listeners
    document.getElementById('drawMode').addEventListener('click', () => setMode('draw'));
    document.getElementById('sprayMode').addEventListener('click', () => setMode('spray'));
    document.getElementById('kaleidoscopeMode').addEventListener('click', () => setMode('kaleidoscope'));
    document.getElementById('gravityMode').addEventListener('click', () => setMode('gravity'));
    
    document.getElementById('clearCanvas').addEventListener('click', clearCanvas);
    document.getElementById('saveArtwork').addEventListener('click', saveArtwork);
    document.getElementById('toggleBackground').addEventListener('click', toggleBackground);
    document.getElementById('helpBtn').addEventListener('click', toggleHelp);
    
    document.getElementById('increaseSize').addEventListener('click', function() {
        brushSize = Math.min(50, brushSize + 1);
        document.getElementById('brushSizeValue').textContent = brushSize;
    });
    
    document.getElementById('decreaseSize').addEventListener('click', function() {
        brushSize = Math.max(1, brushSize - 1);
        document.getElementById('brushSizeValue').textContent = brushSize;
    });
    
    document.getElementById('increaseSymmetry').addEventListener('click', function() {
        symmetry = Math.min(16, symmetry + 1);
        document.getElementById('symmetryValue').textContent = symmetry;
    });
    
    document.getElementById('decreaseSymmetry').addEventListener('click', function() {
        symmetry = Math.max(2, symmetry - 1);
        document.getElementById('symmetryValue').textContent = symmetry;
    });
    
    document.getElementById('helpOverlay').addEventListener('click', toggleHelp);
    
    // Keyboard controls
    document.addEventListener('keydown', function(e) {
        if (e.key === '1') setMode('draw');
        else if (e.key === '2') setMode('spray');
        else if (e.key === '3') setMode('kaleidoscope');
        else if (e.key === '4') setMode('gravity');
        else if (e.key === 'c' || e.key === 'C') clearCanvas();
        else if (e.key === 's' || e.key === 'S') saveArtwork();
        else if (e.key === 'b' || e.key === 'B') toggleBackground();
        else if (e.key === 'h' || e.key === 'H') toggleHelp();
        else if (e.key === 'ArrowUp') {
            brushSize = Math.min(50, brushSize + 1);
            document.getElementById('brushSizeValue').textContent = brushSize;
        }
        else if (e.key === 'ArrowDown') {
            brushSize = Math.max(1, brushSize - 1);
            document.getElementById('brushSizeValue').textContent = brushSize;
        }
        else if (e.key === 'ArrowRight') {
            symmetry = Math.min(16, symmetry + 1);
            document.getElementById('symmetryValue').textContent = symmetry;
        }
        else if (e.key === 'ArrowLeft') {
            symmetry = Math.max(2, symmetry - 1);
            document.getElementById('symmetryValue').textContent = symmetry;
        }
    });
    
    // Animation loop
    function animate() {
        // Update and draw particles
        particles = particles.filter(particle => {
            particle.update();
            if (particle.life > 0) {
                particle.draw();
                return true;
            }
            return false;
        });
        
        requestAnimationFrame(animate);
    }
    
    // Initialize
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();
    setMode('draw');
    animate();
});
