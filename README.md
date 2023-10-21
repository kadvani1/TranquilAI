# TranquilAI - free meditation AI Agent - Relax, Recharge, and Realign: Your Personalized Meditation Experience, Powered by AI and Music

# What is this repo?
Features:
- Generative emotion detection: Detect your current emotions
- Generative music: Generate music from your emotions
- Generative video: Generate video content from your emotions

This README provides an overview of the TranquilAI project and can be added to the project's GitHub repository to provide information to visitors and potential collaborators.

# Technology used

![PeLLM Logo](https://media.licdn.com/dms/image/C560BAQFk_yGavzSPgw/company-logo_200_200/0/1617661228001/hume_ai_logo?e=2147483647&v=beta&t=qczNgjXGUOfy5BrkX9holZ2XXeU4aNzikHVJHhuX7_c)
![PeLLM Logo](https://cdn.mos.cms.futurecdn.net/aSiEWj4bvEGBvUMs9tyXyW.png)
![PeLLM Logo](https://www.thesoftwarereport.com/wp-content/uploads/2023/09/Hugging-Face2.png)

# User Guide
To run, first add your Hume API key to your environment and install the requirements. To run the streamlit demo run: streamlit run st_pellm_demo.py

```python
import asyncio

from hume import HumeStreamClient
from hume.models.config import LanguageConfig

samples = [
    "Mary had a little lamb,",
    "Its fleece was white as snow."
    "Everywhere the child went,"
    "The little lamb was sure to go."
]

async def main():
    client = HumeStreamClient("<your-api-key>")
    config = LanguageConfig()
    async with client.connect([config]) as socket:
        for sample in samples:
            result = await socket.send_text(sample)
            emotions = result["language"]["predictions"][0]["emotions"]
            print(emotions)

asyncio.run(main())
