const int ledPins[4] = {2, 23, 4, 22};  // direita, cima, esquerda, baixo
const int numLeds = 4;
const int freq = 5000;
const int resolution = 8;

void setup() {
  Serial.begin(9600);
  delay(1000);
  Serial.println("Pronto para receber ângulo via Serial.");

  for (int i = 0; i < numLeds; i++) {
    ledcAttach(ledPins[i], freq, resolution);
  }
}

void loop() {
  if (Serial.available()) {
    String data = Serial.readStringUntil('\n');
    data.trim();
    float angle = data.toFloat();
    if (angle >= 0 && angle <= 360) {
      setLedBrightnessByAngle(angle);
    }
  }
}

// -------------------------------
// Brilho suave por decaimento exponencial
// -------------------------------
void setLedBrightnessByAngle(float angle) {
  // centros de cada LED (em graus)
  float centers[4] = {0, 90, 180, 270};
  float sigma = 35; // largura do foco (~quanto o brilho se espalha)

  for (int i = 0; i < numLeds; i++) {
    // diferença circular entre ângulos
    float diff = fmod((angle - centers[i] + 540.0), 360.0) - 180.0; // -180° a +180°

    // intensidade: 1.0 no centro, decai exponencialmente
    float brightness = exp(-0.5 * pow(diff / sigma, 2));

    // corta valores muito baixos
    if (brightness < 0.05) brightness = 0;

    int pwmValue = int(brightness * 255);
    ledcWrite(ledPins[i], pwmValue);
  }
}
