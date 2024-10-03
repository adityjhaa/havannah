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

# Current Progress

## MCTS+UCT vs MCTS+UCT+RAVE

### AI vs RANDOM
> (600s total, board size: 5x5)

#### MCTS + UCT

**Player 2:**
- Win: 453s (fork)
- Loss: 473s (fork)
- Win: 506s (ring)
- Win: 499s (ring)
- Win: 480s (fork)

**Player 1:**
- Loss: 458s (fork) _[Had a win in 2 moves (bridge), missed]_
- Loss: 474s (fork) _[Had a win in 2 moves (ring), missed]_
- Loss: 483s (fork) _[Had a win in 2 moves (bridge), missed]_
- Loss: 463s (bridge) _[Terrible heuristics]_
- Loss: 490s (ring) _[Had a win in 2 moves (bridge), missed]_

#### MCTS + UCT + RAVE

**Player 2:**
- Win: 499s (fork)
- Win: 479s (bridge)
- Win: 473s (ring)
- Win: 493s (fork)
- Win: 453s (bridge) _[Could have done this faster]_

**Player 1:**
- Loss: 513s (bridge) _[Easily winnable, lost due to no blocking and poor threat detection]_
- Win: 495s (ring)
- Win: 548s (bridge)
- Win: 473s (ring)
- Win: 501s (ring)

---

### AI vs AI (MCTS+UCT vs MCTS+UCT+RAVE)

| Player 1 (AI: MCTS+UCT) | Player 2 (AI2: MCTS+UCT+RAVE) |
|-------------------------|-------------------------------|
| 542s, lost         | 549s, won (ring)            |
| 490s, won (bridge)       | 491s, lost            |
| 503s, lost       | 501s, won (bridge)            |
| 490s, lost       | 497s, won (bridge)            |
| 507s, won (bridge)       | 508s, lost            |

#### AI2 (MCTS+UCT+RAVE) as Player 1 vs AI (MCTS+UCT) as Player 2
| Player 1 (AI2)           | Player 2 (AI)                 |
|-------------------------|-------------------------------|
| 496s, won (ring)         | 497s, lost              |
| 453s, lost         | 454s, won (fork)              |
| 463s, won (fork)         | 465s, lost              |
| 474s, lost         | 481s, won (fork)              |
| 507s, won (ring)         | 508s, lost              |

---

#### After Setting params for RAVE and UCT
**Player 2** 
- win bridge 540s 
- win fork 500s
- win fork 506s
- win bridge 513s
- win fork 540s

**Player 1**
- win bridge 513s
- win ridge 561s
- win fork 507s
- win bridge 536s
- win fork 519s

#### After blocking

AI VS AI (AI = RAVE, AI2 = RAVE(0.9, 500) + blocking)
-----------------------------------------------------
| player 1 = AI  | player 2 = AI2 |
|-----------------|----------------|
| (144, lost)    | (145, won) -> fork | 
| (159, lost)    | (161, won) -> bridge |
| (160, lost)    | (162, won) -> bridge |
| (160, lost)    | (162, won) -> bridge |
| (148, lost)    | (149, won) -> bridge |
---
### Notes:
- **AI1 (MCTS+UCT)** demonstrates inconsistent performance, particularly in threat detection and blocking.
- **AI2 (MCTS+UCT+RAVE)** shows generally stronger results, particularly in decision-making when evaluating multiple potential wins.
- Blocking and recognizing win-in-2 moves remains critical to improving heuristics in both algorithms.
- Implementing a multiple rollout strategy is kept as one of the future works.
- LGR, LGRF, N-grams, and Nearest Neighbours approach all remain to be tested.
