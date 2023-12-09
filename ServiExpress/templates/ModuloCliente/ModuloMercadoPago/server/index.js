import express from "express";
import cors from "cors";


// SDK de Mercado Pago
import { MercadoPagoConfig, Preference } from 'mercadopago';
// Agrega credenciales
const client = new MercadoPagoConfig({ accessToken: 'TEST-1613703204369522-120820-11096b34824a004a166273fb25bbd804-116369376' });


const app = express();
const port = 3000;

app.use(cors());
app.use(express.json());

app.get("/", (req,res)=>{
    res.send("Hello World!");
});

app.post("/create_preference", async(req,res)=> {
    try{
        const body = {
            items:[
                {
                title: req.body.title,
                quantity: Number(req.body.quantity),
                unit_price: Number(req.body.price),
                currency_id: "CLP",
            },
        ],
        back_urls: {
            success:"http://http://localhost:8000/index10/",
            failure:"",
            pending:"",
        },
               
    };

    const preference = new Preference(client);
    const result = await preference.create({
        body,
    });
    res.json({
        id: result.id,
    });
    }catch{
        console.log(error)
        res.status(500).json({
            error: "ERROR AL CREAR LA PREFERENCIA"
        })
    }
});

app.listen(port, () =>{
    console.log("el servidor corre")
});

