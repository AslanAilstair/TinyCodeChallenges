const greeting = document.getElementById('greeting');

greeting.addEventListener('click', () => {    
    // Fade out    
    greeting.style.opacity = 0;        
  
    // Change text after fade-out    
    setTimeout(() => {        
        greeting.textContent = greeting.textContent === 'Hello World' ? 'Welcome Back!' : 'Hello World';        
        // Fade in        
        greeting.style.opacity = 1;    
    }, 500); // Match with CSS transition duration
});
