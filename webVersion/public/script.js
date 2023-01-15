
let lifes = 3;
let sprite = document.getElementById("sprite");
let game = document.getElementById("game")
let vel = 20;
let MIN_WIDTH = 0;
let MAX_WIDTH = window.innerWidth-150;
let MAX_HEIGHT=window.innerHeight-50;
let temp_hearts = document.getElementsByClassName("heart")
window.onresize = (ev) => {
    MAX_WIDTH = ev.target.innerWidth-150;
    MAX_HEIGHT = ev.target.innerHeight-50;
 
}
let score = 0;
let score_p = document.getElementById("score")
let popup = document.getElementById("popup")
let hearts =  document.getElementsByClassName("heart");
let level = 5;

let paused = false;
const convert = (val) => {
    return val + "px"
}

var keyState = {};    
window.addEventListener('keydown',function(e){
    if(paused) return;
    keyState[e.keyCode || e.which] = true;
},true);    
window.addEventListener('keyup',function(e){

    keyState[e.keyCode || e.which] = false;
    sprite.style.transform = "rotate(0deg)"
},true);



function gameLoop() {
    let attrSprite = window.getComputedStyle(sprite);
    
    let left_sprite = parseInt(attrSprite.left);
   
    if ((keyState[37] || keyState[65]) && left_sprite >= MIN_WIDTH){
      
                    sprite.style.left = convert(left_sprite-20);
                    sprite.style.transform = "rotate(-90deg)"
                 
    
    }   
    if ((keyState[39] || keyState[68]) && left_sprite <= MAX_WIDTH){
       
                    sprite.style.left = convert(left_sprite+20);
                    sprite.style.transform = "rotate(90deg)"
    
    }

    
    setTimeout(gameLoop, 10);
}    
gameLoop();

     
        setInterval(() => {


if(paused == true) return;

            
let random = Math.round(Math.random() * 10);

if(random <= 10 && random >= 0) {
    let img = document.createElement("img")
    img.setAttribute("src", "./assets/beer.png")
    img.setAttribute("id", "beer")
    img.setAttribute("class", "dispawn")
    img.style.left = convert(Math.random() * MAX_WIDTH);
    game.appendChild(img)
    const interval = setInterval(() => {
        let getCpSt = window.getComputedStyle(img);
        let left_beer = parseInt(getCpSt.left)
        let top_beer = parseInt(getCpSt.top);
        let attrSprite = window.getComputedStyle(sprite);
        let left_sprite = parseInt(attrSprite.left);
            let top_sprite = parseInt(attrSprite.top)
        if(Math.abs(top_beer / 2 - top_sprite / 2) <= 50 && Math.abs(left_beer / 2 - left_sprite / 2) <= 50) {
            level++;
            let audio = new Audio("./assets/take.wav");
            audio.play()
            score++;
            score_p.textContent = score;
            vel+=5;
            sprite.style.filter = `saturate(${level})`
            clearInterval(interval);
            img.parentNode.removeChild(img)
        }
        if(top_beer >= MAX_HEIGHT) {
            img.parentNode.removeChild(img)
            lifes--;
            hearts[hearts.length-1].remove()
            
            if(lifes == 0) {
              let beers = document.getElementsByClassName("dispawn")
         for(let i=0; i<beers.length;i++) {
            beers[i].remove()
         }
         for(let i=0;i<temp_hearts.length;i++) {
            document.getElementById("hearts").appendChild(temp_hearts[i])
         }
         document.getElementById("final_score").textContent = score;
            vel = 20;
            popup.style.display = "flex";
          paused = true;
score = 0;
score_p.textContent = score;
            clearInterval(interval);
            return;
            }
        
        }
        setTimeout(() => {img.style.top = convert(top_beer+vel)},10)
        
        
    }, 100)
} else {
    return;
}

        }, 3000)
