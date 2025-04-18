import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

def count_tokens(text: str) -> int:
    token_ids = encoding.encode(text)
    return len(token_ids)