const mp = new MercadoPago('TEST-8f404af3-bf66-40a8-8aca-92df4d060f83',{
    locale: "es-CL",    
});

document.getElementById("checkout-btn").addEventListener("click", async() =>{
    try{
        const orderData = {
        title: "Mantenimiento 30.000 kms",
        quantity: 1,
        price: 100000
    };

    const response = await fetch("http://localhost:3000/create_preference", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(orderData),
    });

    const preference = await response.json()
    createCheckoutButton(preference.id);
    }catch(error){
        alert("error:(");
    }
});

const createCheckoutButton = (preferenceId) => {
    const bricksBuilder = mp.bricks();

    const renderComponent = async () => {
        if(window.checkoutbutton) window.checkoutbutton.unmount();

        await bricksBuilder.create("wallet", "wallet_container", {
            initialization: {
                preferenceId: preferenceId,
            },
         });
    };

    renderComponent();
};