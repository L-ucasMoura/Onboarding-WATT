

const IP = "http://10.7.240.9:5000"
const ngrokIP = 'https://dusty-nonfeasible-marisha.ngrok-free.dev'

export const toEsp = async (angle:number, direction:string) => {
  try{
    const response = await fetch(`${IP}/server/toEsp`,{
      method: 'POST',
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({direction, angle}),
    });
    
    const data = await response.json();
    return data;
  }
  catch (error) {
    console.error("Erro ao enviar dado", error);
    throw error;
  }
};

export const toTable = async (x:number, y:number, z:number, angle:number, direction:string) => {
  try{
    const response = await fetch(`${IP}/server/gotodb`,{
      method: 'POST',
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({x, y, z, direction, angle}),
    });
    
    const data = await response.json();
    return data;
  }
  catch (error) {
    console.error("Erro ao enviar dado", error);
    throw error;
  }
};
