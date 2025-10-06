
export const enviarDado = async (x:Number, y:Number, z:Number) => {
  try{
    const response = await fetch("http://192.168.1.8:5000/gotodb",{
      method: 'POST',
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({x, y, z}),
    });
    
    const data = await response.json();
    console.log("Resposta do Servidor", data);
    return data;
  }
  catch (error) {
    console.error("Erro ao enviar dado", error);
    throw error;
  }
};