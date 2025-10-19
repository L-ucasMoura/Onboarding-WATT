import { Accelerometer } from "expo-sensors";
import { useEffect, useState, useRef } from "react";
import { Text, View, StyleSheet } from "react-native";
import { MaterialCommunityIcons } from "@expo/vector-icons";
import { toEsp, toTable } from "./api";
import {getDirection} from "./appFunctions";

export default function Index() {
  
  const [{ x, y, z }, setData] = useState({ x: 0, y: 0, z: 0 });
  
  const dataRef = useRef({ x: 0, y: 0, z: 0 });

  const angle = (x, y) => {
    const a = Math.atan2(y, -x) * (180 / Math.PI);
    return (a + 360) % 360;
  };

  // Atualiza o estado e envia pra ESP em tempo real
  useEffect(() => {
    const subscription = Accelerometer.addListener((dados) => {
      setData(dados);
      dataRef.current = dados; // <-- mantém os valores mais recentes

      const direction = getDirection(angle(dados.x, dados.y));
      const angulo = angle(dados.x, dados.y);
      //toEsp(angulo, direction);
    });

    Accelerometer.setUpdateInterval(100);
    return () => subscription.remove();
  }, []);

  // Envia pro banco a cada 1 segundo
  let count = 0;
  useEffect(() => {
    const interval = setInterval(() => {
      const { x, y, z } = dataRef.current;
      const direction = getDirection(angle(x, y));
      const angulo = angle(x, y);

      console.log("⏱ Enviando pro banco...", { x, y, z, angulo, direction });
      toTable(x, y, z, angulo, direction);

      if(count % 3 === 0){
        console.log('Enviando pra ESP')
        toEsp(angulo, direction)
      }
      count += 1;
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  const direction = getDirection(angle(x, y));

  const getIcon = () => {
    switch (direction) {
      case "UP": return "arrow-up-bold";
      case "DOWN": return "arrow-down-bold";
      case "LEFT": return "arrow-left-bold";
      case "RIGHT": return "arrow-right-bold";
      default: return "compass";
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>📱 Dados do Acelerômetro</Text>

      <View style={styles.box}>
        <Text style={styles.text}>X: {x.toFixed(3)}</Text>
        <Text style={styles.text}>Y: {y.toFixed(3)}</Text>
        <Text style={styles.text}>Z: {z.toFixed(3)}</Text>
      </View>

      <Text style={styles.angle}>Ângulo: {angle(x, y).toFixed(1)}°</Text>
      <Text style={styles.direction}>Direção: {direction}</Text>

      <MaterialCommunityIcons
        name={getIcon()}
        size={80}
        color="#0D47A1"
        style={{ marginTop: 20 }}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#E3F2FD",
    alignItems: "center",
    justifyContent: "center",
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: "bold",
    color: "#0D47A1",
    marginBottom: 20,
  },
  box: {
    backgroundColor: "#BBDEFB",
    borderRadius: 16,
    padding: 16,
    elevation: 4,
    width: "90%",
  },
  text: {
    fontSize: 18,
    color: "#1A237E",
  },
  angle: {
    fontSize: 20,
    fontWeight: "600",
    marginTop: 20,
  },
  direction: {
    fontSize: 22,
    color: "#0D47A1",
    fontWeight: "700",
    marginTop: 8,
  },
});