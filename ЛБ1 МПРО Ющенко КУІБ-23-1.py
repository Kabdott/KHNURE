import asyncio
from telethon import TelegramClient

API_ID =
API_HASH = ""

client = TelegramClient("my_session", API_ID, API_HASH)


async def main():
    await client.start()

    print("1. Лист учасників групи")
    print("2. Надіслати повідомлення")
    choice = input("Оберіть дію: ")

    try:
        if choice == "1":
            chat = input("Ім'я групи: ")

            participants = await client.get_participants(chat)

            print(f"\nУчасники групи: {len(participants)}")

            for user in participants:
                name = " ".join(
                    part for part in [user.first_name, user.last_name]
                    if part
                )
                print(f"ID: {user.id} | Ім'я: {name}")

        elif choice == "2":
            recipient = input(
                "@username контакта чи групи: "
            )
            message = input("Текст повідомлення: ")

            await client.send_message(recipient, message)

    finally:
        await client.disconnect()


asyncio.run(main())
