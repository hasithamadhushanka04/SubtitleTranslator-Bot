from pyrogram.types import InlineKeyboardButton
from creds import cred

welcome = (
    "**ඔබට translate කිරීමට අවශ්‍ය උපසිරැසිය මට ලබා දෙන්න.**"
    "\n**කරුණාකර, මෙම බොට්ගේ updates පිළිබඳව දැනගන්න අපගේ ප්‍රධාන චැනලයට එක් වෙන්න.@CloudUpdateslk** "
)
about = (
    "**මෙම බොට් මගින් ඔබට කුමක් හෝ භාශාවකින් තිබෙන උපසිරසියක් තවත් භාෂාවකට පරිවර්තනය කල හැක**"
    "\n**To Back : /start** "
)
help_text = (
    "**අනුගමනය කළ යුතු පියවර**\n\n**මේක subtitle translator bot එකක්**\n**1. පරිවර්තනය කිරීම සඳහා උපසිරැසි ගොනුව මට එවන්න.** "
    "\n**2. පරිවර්තනය කල යුතු භාෂාව තෝරන්න (බොත්තම් කිහිපයක් ඔබන්න එපා).**\n**3. පරිවර්තනය සම්පූර්ණ කිරීමට යම් කාලයක් රැඳී සිටින්න.** "
    "\n\n**මතක තබා ගන්න**\n\n**1. ඔබට එකවර පරිවර්තනය කළ හැක්කේ එක් උපසිරැසියක් පමණි** "
    "\n**2. උපසිරැසි ගොනු කිහිපයක් එකවර යොමු නොකරන්න.** "
    "\n**To Back : /start** "
)
eta_text = (
    "**File name :** `{}`\n**Done** `{}` **of** `{}`\n**Percentage:** {}%\n**Speed:** {} lines/sec\n**ETA:** {}\n[{"
    "}{}] "
)
caption = f"Translated by {cred.BOT_NAME}"
empty = "`You need to send a subtitle(srt) file inorder to translate it`"
mmtypes = [
    "text/plain",
    "application/x-subrip",
    "application/octet-stream",
    "application/binary",
]
err1 = "**__One subtitle is processing wait sometime__**"
err2 = "**__This is not a subtitle(srt) file__**"
err3 = "**Todays limit exceeded**"
err4 = "**Unsupported characters in file**"
err5 = "**Some errors happened Try again..**"

langs = [
    [
        InlineKeyboardButton("മലയാളം", callback_data="Malayalam"),
        InlineKeyboardButton("தமிழ்", callback_data="Tamil"),
        InlineKeyboardButton("हिन्दी", callback_data="Hindi"),
    ],
    [
        InlineKeyboardButton("ಕನ್ನಡ", callback_data="Kannada"),
        InlineKeyboardButton("తెలుగు", callback_data="Telugu"),
        InlineKeyboardButton("मराठी", callback_data="Marathi"),
    ],
    [
        InlineKeyboardButton("ગુજરાતી", callback_data="Gujarati"),
        InlineKeyboardButton("ଓଡ଼ିଆ", callback_data="Odia"),
        InlineKeyboardButton("বাংলা", callback_data="bn"),
    ],
    [
        InlineKeyboardButton("ਪੰਜਾਬੀ", callback_data="Punjabi"),
        InlineKeyboardButton("فارسی", callback_data="Persian"),
        InlineKeyboardButton("English", callback_data="English"),
    ],
    [
        InlineKeyboardButton("español", callback_data="Spanish"),
        InlineKeyboardButton("français", callback_data="French"),
        InlineKeyboardButton("русский", callback_data="Russian"),
    ],
    [
        InlineKeyboardButton("עִברִית", callback_data="hebrew"),
        InlineKeyboardButton("العربية", callback_data="arabic"),
        InlineKeyboardButton("සිංහල",callback_data="sinhala"),
    ],
]
