import { Accelerometer } from "expo-sensors";
import { useEffect, useState } from "react";
import { Text, View } from "react-native";

export default function Index() {
    const [{x, y, z}, setData] = useState({x: 0, y: 0, z: 0});

    useEffect(() => {
        const subscription = Accelerometer.addListener(setData);
        return () => subscription.remove();
    }, []);

    Accelerometer.setUpdateInterval(500);

    const radToDeg = (rad: number) => rad * (180 / Math.PI);

  function getAngles(x: number, y: number, z: number) {
    const pitch = radToDeg(Math.atan2(x, Math.sqrt(y * y + z * z)));
    const roll = radToDeg(Math.atan2(y, Math.sqrt(x * x + z * z)));

    return {
      pitch: Number(pitch.toFixed(2)),
      roll: Number(roll.toFixed(2)),
    };
  }

  const { pitch, roll } = getAngles(x, y, z);

  return (
    <View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
      <Text>Pitch: {pitch}°</Text>
      <Text>Roll: {roll}°</Text>
    </View>
  );
}
