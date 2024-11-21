import asyncio

from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions
from viam.components.camera import Camera
from viam.services.mlmodel import MLModelClient
from viam.services.vision import VisionClient

async def connect():
    opts = RobotClient.Options.with_api_key( 
        api_key='o6dxrbeftpcj5ceze7jvh9qbcu240g7k',
        api_key_id='010159c7-334b-4d46-9707-bc8f100a3466'
    )
    return await RobotClient.at_address('viamvision-main.ei59t0va5a.viam.cloud', opts)

async def main():
    machine = await connect()

    print('Resources:')
    print(machine.resource_names)
    
    # Macbook-Pro
    macbook_pro = Camera.from_robot(machine, "Macbook-Pro")
    macbook_pro_return_value = await macbook_pro.get_image()
    print(f"Macbook-Pro get_image return value: {macbook_pro_return_value}")

    # people
    people = MLModelClient.from_robot(machine, "people")
    people_return_value = await people.metadata()
    print(f"people metadata return value: {people_return_value}")

    # myPeopleDetector
    my_people_detector = VisionClient.from_robot(machine, "myPeopleDetector")
    my_people_detector_return_value = await my_people_detector.get_properties()
    print(f"myPeopleDetector get_properties return value: {my_people_detector_return_value}")

    # Don't forget to close the machine when you're done!
    await machine.close()

if __name__ == '__main__':
    asyncio.run(main())
