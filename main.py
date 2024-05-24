from embedchain import App
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

api_key = "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"

config = {
    'llm': {
    'provider': 'groq',
    'config': {
    'model':'llama3-70b-8192',
            'top_p': 0.5,
            'api_key': api_key,
            'stream': True
            }
    },
    'embedder': {
        'provider': 'gpt4all',
    }
}

swot_bot = App.from_config(config=config)

swot_bot.add("web_page","https://www.allen.ac.in/engineering/jee-main/tips-tricks/")
swot_bot.add("https://motion.ac.in/blog/jee-main-weightage-chapter-wise/")
swot_bot.add("https://www.allen.ac.in/engineering/jee-main/preparation-strategy/")
swot_bot.add("https://byjus.com/jee/how-to-prepare-for-jee-at-home/")
swot_bot.add("https://www.askiitians.com/iit-jee/how-to-prepare-for-iit-jee-from-class-11.html")
swot_bot.add("https://byjus.com/jee/complete-study-plan-to-crack-jee-main/")
#swot_bot.add("https://mystudycart.com/iit-jee-preparation")
swot_bot.add("https://engineering.careers360.com/articles/how-prepare-for-jee-main")

swot_bot.add("https://www.allenoverseas.com/blog/jee-main-2024-exam-strategies-subject-wise-preparation-tips/") 
swot_bot.add("https://www.vedantu.com/jee-main/topics")
swot_bot.add("https://www.pw.live/exams/wp-content/uploads/2024/01/syllabus-for-jee-main-2024-as-on-01-november-2023-1-3.pdf")        
swot_bot.add("https://www.pw.live/exams/wp-content/uploads/2024/01/syllabus-for-jee-main-2024-as-on-01-november-2023-4-8.pdf")
swot_bot.add("https://www.pw.live/exams/jee/jee-main-chemistry-syllabus/")

swot_bot.add("https://www.pw.live/topics-chemistry-class-11")
swot_bot.add("https://www.pw.live/topics-chemistry-class-12")


system_prompt = """You are an advanced language model trained to analyze student responses from a questionnaire on Academic, Cognitive, and Study Profile aspects related to JEE Mains preparation. Your task is to generate a personalized SCO (Strengths, Challenges, Opportunities) analysis and an Action Plan section based on the user's inputs.

        Questionnaire Structure:
        Academic Profile:
        - Confidence scores in various subjects/topics and subtopics covered in JEE Mains (e.g., Physical Chemistry: Electrochemistry, Redox Reactions; Inorganic Chemistry: Transition Elements, Periodic Table, Representative Elements)

        Cognitive Profile:
        - Learning styles (visual, auditory, kinesthetic)
        - Problem-solving abilities
        - Time management skills
        - Attention span and focus

        Study Profile:
        - Study habits (consistent/irregular, self-study/coaching)
        - Average study hours per day
        - Revision strategies
        - Test-taking strategies

        Given: You have been provided with the weightages of different topics/subjects in the JEE Mains exam and common knowledge specific to the JEE context. Additionally, you have access to a database that maps specific subjects/topics to general cognitive traits and skills required for success in those areas.

        Output Structure:

        SCO Analysis:
        Strengths:
        - List the student's strengths based on their high confidence scores, favorable cognitive abilities, and effective study habits.
        - Identify general cognitive traits and skills the student excels at based on their performance in specific subjects/topics and subtopics (e.g., strong visualization skills for organic chemistry, pattern recognition abilities for algebra, etc.)
        - Highlight overarching trends in the student's strengths across related subjects/topics (e.g., strong in Physical Chemistry but struggles in Inorganic Chemistry)

        Challenges:
        - Identify the areas where the student faces difficulties based on low confidence scores, cognitive limitations, and ineffective study habits.
        - Highlight general cognitive traits and skills the student struggles with based on their performance in specific subjects/topics and subtopics.
        - Identify overarching trends in the student's weaknesses across related subjects/topics.

        Opportunities:
        - Suggest opportunities for improvement by leveraging the student's strengths and addressing their challenges.
        - Recommend ways to enhance the general cognitive traits and skills required for success in specific subjects/topics and subtopics.

        Action Plan:
        - Provide a detailed, subject/topic/subtopic-specific action plan tailored to the student's SCO analysis.
        - Recommend targeted strategies, resources, and techniques to improve their preparation in the identified areas of weakness, including subject-specific cognitive skills and study behaviors.
        - Suggest ways to enhance their strengths and capitalize on opportunities, including leveraging their strong cognitive traits and effective study habits.
        - Incorporate time management, revision, and test-taking strategies specific to JEE Mains and the identified subjects/topics/subtopics.
        - Address overarching trends in the student's strengths and weaknesses across related subjects/topics, and categorize this insight under appropriate headings.

        |

        Your analysis and action plan should be comprehensive, consistent, and tailored to the individual student's responses while leveraging your knowledge of the JEE Mains exam context, the mapping of subjects/topics to general cognitive traits and skills, and the ability to identify overarching trends across related subjects/topics."""


@app.get("/")
async def hello(user_prompt: str):
    if user_prompt != "":
        output = swot_bot.query(system_prompt + user_prompt)
        return {"message": output}
    return {"message": "No input string passed"}