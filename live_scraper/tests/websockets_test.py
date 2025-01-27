import asyncio
import websockets
import json


async def test_websocket():
    uri = "ws://127.0.0.1:8000/ws/live/"
    async with websockets.connect(uri) as websocket:
        # Enviar uma mensagem
        message = {"message": "Testando o WebSocket!"}
        await websocket.send(json.dumps(message))
        print(f"Mensagem enviada: {message}")

        # Receber a resposta
        response = await websocket.recv()
        print(f"Resposta recebida: {response}")


asyncio.run(test_websocket())
