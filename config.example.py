import colors

TOKEN = "nuh uh you dont get to see my token"

BOT_PREFIX = "."
LOG_PREFIX = f"[{colors.RED}Cranberry{colors.END}Bot]"

IMPOSSIBLE_GAMES = False

CAT_API_KEY = "you dont get to"
DOG_API_KEY = "see my api keys either"
RAPIDAPI_KEY = "no not this either"

FACTS_ROUTE = "https://uselessfacts.jsph.pl/api/v2/facts/random"
CATS_ROUTE = "https://api.thecatapi.com/v1/images/search"
DOGS_ROUTE = "https://api.thedogapi.com/v1/images/search"
MEMES_ROUTE = "https://meme-api.com/gimme"
WYR_HOST = "would-you-rather.p.rapidapi.com"
WYR_ROUTE = f"https://{WYR_HOST}/wyr/random"


def nsfw_route(category: str, content_type: str) -> str:
    return f"https://purrbot.site/api/img/nsfw/{category}/{content_type}"
