
export const enviarDado = async (angle:number, direction:string) => {
  try{
    //"http://192.168.1.8:5000/gotodb"
    const response = await fetch("http://10.7.240.9:5000/listener",{
      method: 'POST',
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({direction, angle}),
    });
    
    const data = await response.json();
    //console.log("Resposta do Servidor", data);
    return data;
  }
  catch (error) {
    console.error("Erro ao enviar dado", error);
    throw error;
  }
};
