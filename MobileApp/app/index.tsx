import { Accelerometer } from "expo-sensors";
import { useEffect, useState } from "react";
import { Text, View } from "react-native";
import { enviarDado } from "./api";
import getDirection from "./getAngle";


export default function Index() {
  
  const [{x, y, z}, setData] = useState({x: 0, y: 0, z: 0});
  
  
  // Obtém o ângulo de 0 à 360
  const angle = (x:number, y:number) => {
    const a = Math.atan2(y,-x) * 180/Math.PI
    return ((a+360) % 360);
  }

  
  useEffect(() => {
    const subscription = Accelerometer.addListener((dados) => {
      setData(dados);
      const direction = getDirection(angle(dados.x,dados.y));
      
      enviarDado(angle(y,-x), direction);
      });
      return () => subscription.remove();
    }, []);
    
    Accelerometer.setUpdateInterval(100);
    
  const direction = getDirection(angle(x,y));


  return (
    <View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
      <Text>Pitch: {angle(x, y).toFixed(1)}°</Text>
      <Text>Direção: {direction}</Text>
      
    </View>
  );
}
