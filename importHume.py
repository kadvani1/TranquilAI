import asyncio

from hume import HumeStreamClient, StreamSocket
from hume.models.config import FaceConfig

async def main():
    client = HumeStreamClient("<your-api-key>")
    config = FaceConfig(identify_faces=True)
    async with client.connect([config]) as socket:
        result = await socket.send_file("<your-image-filepath>")
        print(result)

asyncio.run(main())