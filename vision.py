import os
from dotenv import load_dotenv
import asyncio
from PIL import Image

from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions
from viam.components.camera import Camera
from viam.media.utils.pil import viam_to_pil_image


async def connect():
    opts = RobotClient.Options.with_api_key( 
        api_key='iqr8me7dpa5f0oxwtkdnn88f9ja07x9v',
        api_key_id='ece56106-2f96-4724-bee3-35a3167b3d2c'
    )
    return await RobotClient.at_address('viamvision-main.ei59t0va5a.viam.cloud', opts)

async def main():
    # Connect to the VIAM webcam machine
    machine = await connect()
    # Print resources
    print('Resources:')
    print(machine.resource_names)
    # MacBook-Pro-Webcam
    mac_book_pro_webcam = Camera.from_robot(machine, "MacBook-Pro-Webcam")
    # take snapshot
    mac_book_pro_webcam_return_value = await mac_book_pro_webcam.get_image()
    # Print metadata
    print(f"MacBook-Pro-Webcam get_image return value: {mac_book_pro_webcam_return_value}")
    # Show snapshot
    snapshot = viam_to_pil_image(mac_book_pro_webcam_return_value)
    snapshot.show()
    await machine.close()

if __name__ == '__main__':
    load_dotenv()
    asyncio.run(main())
