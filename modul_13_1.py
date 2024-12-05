import asyncio

async def start_starongman(name, power):
    num = 1
    timme = 6
    print(f"Силач {name} начал соревнования.")
    while num <= 5:
        await asyncio.sleep(timme - power)
        print(f"Силач {name} поднял {num}")
        num += 1
    print(f"Силач {name} закончил соревнования")

async def main():
    pasha = asyncio.create_task(start_starongman('Pasha', 3))
    dasha = asyncio.create_task(start_starongman('Denis', 4))
    apolon = asyncio.create_task(start_starongman('Apollon', 5))
    await pasha
    await dasha
    await apolon

asyncio.run(main())
