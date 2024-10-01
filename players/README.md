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
