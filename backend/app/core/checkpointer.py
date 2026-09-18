from langgraph.checkpoint.memory import MemorySaver

# In-memory checkpointer for multi-turn conversational session states
# Can be seamlessly replaced with PostgresSaver or RedisSaver in production
memory_checkpointer = MemorySaver()
