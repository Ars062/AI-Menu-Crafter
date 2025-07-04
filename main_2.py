from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import os


llm = Ollama(model="gemma:2b") 








def generate_restaurant_name_and_menu_(name):
    # "Bistro" is a small, casual restaurant.
    # "Tacos", "Burritos", and "Nachos" are popular Mexican dishes:
    # - Taco: a folded tortilla filled with meat, cheese, and vegetables.
    # - Burrito: a large tortilla wrapped around fillings like beans, rice, and meat.
    # - Nachos: tortilla chips topped with melted cheese and other toppings.
    prompt_template = PromptTemplate(
    input_variables=["name"],
    template="I want to open a {name} food restaurant, Suggest only one restaurant name for it, please avoid any kind of descrption for it,just return the name only .",
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template, output_key="restaurant_name")
    # response = chain.invoke({"name": "mexican"})
    prompt_template_items= PromptTemplate(
        input_variables=["restaurant_name"],
        template="""suggest some food menu items for a food restaurant named {restaurant_name} food,without any descriptions or extra text or introductory word like 'sure,here is a list of food menu items based on the suggestion:', return it as a comma separated list .""",
    )
    items_chain = LLMChain(llm=llm, prompt=prompt_template_items,output_key="menu_items")
    sequential_chain = SequentialChain(chains=[name_chain, items_chain], input_variables=["name"], output_variables=["restaurant_name", "menu_items"], verbose=True)
    result = sequential_chain.invoke({"name": name})
    return result

if __name__ == "__main__":
    name = "indian"
    result = generate_restaurant_name_and_menu_(name)
    print(f"Restaurant Name: {result['restaurant_name']}")
    print(f"Menu Items: {result['menu_items']}")