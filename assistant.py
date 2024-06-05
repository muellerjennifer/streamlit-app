"""
Liste mit Custom GPTs
"""

import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())


# Insert your assistant id
OPENAI_ASSISTANT = 'asst_9N03do2t5NilKzstTMDXSk4T'


gpts = {
    "CustomGPT": OPENAI_ASSISTANT,
}