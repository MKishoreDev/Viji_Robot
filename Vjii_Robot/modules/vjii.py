import random
from Vjii_Robot import pbot as bot
from pyrogram import filters
from pyrogram.types import Message

VJII = (
"If your stuffed animals could talk, what would they say?",
"What does it feel like when I hug you?",
"If you drew everything that came to your head, what would you be drawing right now?",
"What do you think you're going to dream about tonight?",
"What sounds do you like?",
"You're outside for a whole day: what would you do?",
"What makes the best fort?",
"How do you think animals communicate?",
"Describe a great day. What are you doing that makes it special?",
"What animal would make a great driver?",
"Do you like it when other people share with you? Why?",
"Who is your favorite storybook character?",
"What one thing do you do now that you need an adult for but would like to try to do all by yourself?",
"If you had to give everyone in the family new names, what would they be?",
"What makes you happy?"
"If you could do anything right now, what would you do?",
"If you had a pet dragon, what would you name it?",
"What would you do together?",
"Do you ever think about renaming the colors of your crayons?",
"What character makes you laugh the most?",
"If you opened a store, what would you sell?",
"What's your superhero name and what powers do you have?",
"If you could grow anything in the yard, what would it be?",
"What do you enjoy giving people?",
"Did you smile or laugh extra today?",
"Pretend you're a chef, and tell me about your restaurant. What foods do you serve?",
"Where would you like to travel? How would you get there?",
"If you could ask a wild animal any question, what would you ask?",
"What are some of the best things about nature?",
"You're a photographer for a day, what would you take pictures of?",
"What bugs you?",
"Do you have any inventions in your brain?",
"Do you think it'd be fun to learn another language?",
"If you could make up a new holiday, what would it be?",
"What is the craziest thing you've ever eaten?",
"Come up with three silly new traditions for the world. Or for aliens on another planet!",
"What would you do if you made the rules at home?"
"What makes someone smart?",
"What do you like daydreaming about?",
"Tell me something about you that you think I might not know.",
"What have your friends been up to?",
"What's a memory that makes you happy?",
"What do you look forward to when you wake up?",
"You're at the beach. What's the first thing you do?",
"What makes you feel brave?",
"What makes you feel loved?",
"How do you show people you care?",
"If you could give $100 to a charity, which would you choose?",
"How would you design a treehouse?",
"If you wrote a book, what would it be about?",
"If you designed clothes, what would they look like?",
"How do you best like helping others?",
"What makes you feel thankful?",
"If you made a cave in the woods, what would be inside it?",
"What makes you feel energized?",
"If you were in a play, what would your character be like?",
"What makes your friends so awesome?",
"What makes you so awesome?",
"What are three things you want to do this summer?",
"If you had friends all over the world, how would you keep in touch?",
"If you joined the circus, what would your circus act be?",
"If you were a teacher and could teach your students anything at all, what would you teach them?",
"If a friend asks you to keep a secret that you don't feel comfortable keeping, what would you do?",
)

@bot.on_message(
    (filters.document
     | filters.text
     | filters.photo
     | filters.sticker
     | filters.animation
     | filters.video)
    & ~filters.private,
    group=8,
)
async def vjiiii(_, message): 
    if message.reply_to_message == 5107947003:
         await message.reply_text(random.choice(VJII))
    else:
         return
