# Current Stats

- **AI: RAVE(0.9, 500) with lookahead + blocking + 10 rollouts**
- **AI2: RAVE(0.9, 500) with lookahead + blocking + 5 rollouts**

## AI Vs Random
> (5x5 & 240s)

1. AI as Player 1

- Won : 216s (ring)
- Won : 219s (ring)
- Won : 221s (fork)
- Won : 211s (ring)
- Won : 216s (bridge)

2. AI as Player 2

- Won : 210s (bridge)
- Won : 212s (bridge)
- Won : 205s (bridge)
- Won : 204s (bridge)
- Won : 207s (bridge)

## AI Vs AI2
> (4x4 & 300s)

1. AI as Player 1

|  Player 1 (AI)  |  Player 2 (AI2)  |
|-----------------|------------------|
| Lost, 267s  | Won, 275s (bridge)   |
| Lost, 271s  | Won, 275s (bridge)   |
| Won, 271s (bridge)  | Lost, 275s   |
| Lost, 245s    | Won, 264s (fork)   |
| Won, 275s (fork)    | Lost, 279s   |

2. AI as Player 2

|  Player 1 (AI2)  |  Player 2 (AI)  |
|------------------|-----------------|
| Lost, 275s  | Won, 259s (bridge)   |
| Lost, 279s  | Won, 275s (bridge)   |
| Lost, 275s  | Won, 263s (bridge)   |
| Lost, 275s  | Won, 275s (bridge)   |
| Won, 279s (bridge)  | Lost, 275s   |

## AI Vs AI2
> (6x6 & 500s)

1. AI as Player 1

|  Player 1 (AI)  |  Player 2 (AI2)  |
|-----------------|------------------|
| Won, 411s (fork)     | Lost, 405s  |
| Won, 422s (fork)     | Lost, 432s  |
| Won, 418s (fork)     | Lost, 433s  |
| Won, 427s (bridge)   | Lost, 432s  |
| Won, 447s (bridge)   | Lost, 457s  |

2. AI as Player 2

|  Player 1 (AI2)  |  Player 2 (AI)  |
|------------------|-----------------|
| Won, 397s (fork)     | Lost, 381s  |
| Lost, 460s  | Won, 460s (ring)     |
| Won, 427s (fork)     | Lost, 411s  |
| Won, 420s (fork)     | Lost, 416s  |
| Won, 416s (bridge)   | Lost, 419s  |

