import { Accelerometer } from "expo-sensors";
import { useEffect, useState } from "react";
import { Text, View } from "react-native";
import { enviarDado } from "./api";

export default function Index() {
  const [{x, y, z}, setData] = useState({x: 0, y: 0, z: 0});

  useEffect(() => {
      const subscription = Accelerometer.addListener((dados) => {
        setData(dados);
        enviarDado(dados.x, dados.y, dados.z);
      });
      return () => subscription.remove();
  }, []);

  Accelerometer.setUpdateInterval(1000);

  return (
    <View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
      <Text>X: {x}</Text>
      <Text>Y: {y}</Text>
      <Text>Z: {z}</Text>
    </View>
  );
}
