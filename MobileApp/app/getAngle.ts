
// cima-baixo: y
// direita-esquerda: x
// frente-verso: z

//pitch: Inclinação frente-trás
//roll: Inclinação direita-esquerda

export default function getDirection(angle: number){
  if (angle >= 45 && angle < 135){
    //console.log("Up")
    return "UP"
  }
  else if(angle >= 135 && angle < 225){
    //console.log("Left")
    return "LEFT"
  }
  else if(angle >= 225 && angle <=315){
    //console.log('Down')
    return 'DOWN'
  }
  else{
    //console.log('Right')
    return 'RIGHT'
  }
}