#!/usr/bin/env python3
import asyncio

async def alice_task():
    print("Alice is working on her task")
    await asyncio.sleep(2)  # Simulating some asynchronous work
    print("Alice finished her task")

async def bob_task():
    print("Bob is working on his task")
    await asyncio.sleep(3)  # Simulating some asynchronous work
    print("Bob finished his task")

async def carol_task():
    print("Carol is working on her task")
    await asyncio.sleep(1)  # Simulating some asynchronous work
    print("Carol finished her task")

async def main():
    # Using asyncio.gather to execute tasks in parallel
    await asyncio.gather(alice_task(), bob_task(), carol_task())

# Running the main function
asyncio.run(main())
