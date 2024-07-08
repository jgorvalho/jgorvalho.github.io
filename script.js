document.addEventListener('DOMContentLoaded', (event) => {
    // Função para subscrever ao tópico MQTT
    function subscribeToMQTT() {
        // Configurações do broker MQTT
        const brokerUrl = 'mqtt://mqtt.streamline.pt:1883';
        const options = {
            username: 'mwg',
            password: '6KbTvz7b9XxS',
        };
        const topic = 'application/4e85f534-31b7-4f51-ba15-2ecd63e5f5f5/device/a84041feb1875df6/event/up';

        // Conectar ao broker MQTT
        const client = mqtt.connect(brokerUrl, options);

        // Evento quando a conexão é bem-sucedida
        client.on('connect', () => {
            console.log('Conectado ao broker MQTT');
            // Subscrever ao tópico
            client.subscribe(topic, (err) => {
                if (!err) {
                    console.log(`Inscrito no tópico ${topic}`);
                } else {
                    console.error('Erro ao subscrever no tópico', err);
                }
            });
        });

        // Evento quando uma mensagem é recebida
        client.on('message', (topic, message) => {
            const receivedMessage = message.toString();
            console.log('Mensagem recebida:', receivedMessage);
            // Atualizar o conteúdo do elemento HTML com a mensagem recebida
            document.getElementById('message-value').innerText = receivedMessage;
        });

        // Evento de erro
        client.on('error', (error) => {
            console.error('Erro na conexão MQTT:', error);
        });
    }

    // Chamar a função para subscrever ao tópico MQTT
    subscribeToMQTT();
});
