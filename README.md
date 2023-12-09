# Dirty Santa
A competitive framework for the Dirty Santa gift exchange. This project is perfect for participants to develop reinforcement learning agents.

# Context
Dirty Santa, also known as Yankee Swap, White Elephant, or Secret Santa, is a popular holiday gift exchange game played in groups. The game is often used as a fun and entertaining way for people to exchange gifts within a social or office setting. Here's a general overview of how Dirty Santa typically works:

**Participants**: A group of people agrees to participate in the gift exchange.

**Gift Selection**: Participants are asked to bring a gift to the event. Generally, there is a predefined budget. In this project, we will assume a common agreement on how the gifts rank in terms of preference (there's a gift everybody would love to have, a gift that everybody hates, and everything in the middle).

**Number Assignment**: Participants draw numbers to determine the order in which they will select a gift. The first person selects a wrapped gift and opens it.

**Subsequent Turns**: The following participants can either choose a new, wrapped gift from the pile or "steal" an already opened gift from someone else. If a gift is stolen, the person whose gift was taken can then choose a new gift. In some versions (not this one), the person can steal a gift from another person.

**End of Game**: The game continues until everyone has had a turn or until there are no more gifts to be chosen. The last person to pick a gift may have the option to make a final steal.