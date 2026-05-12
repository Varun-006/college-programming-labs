# 9. Take the Institution name as input. Use Pydantic to define the schema for the desired output and create a custom output parser. Invoke the Chain and Fetch Results. Extract the below Institution related details from Wikipedia: The founder of the Institution. When it was founded. The current branches in the institution. How many employees are working in it. A brief 4-line summary of the institution. 

from pydantic import BaseModel 
import wikipediaapi 
class InstitutionInput(BaseModel): 
    institution_name: str 
def fetch_institution_details(institution_name: str): 
    wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        user_agent='MyApp/1.0 (example@example.com)'
    ) 
    page = wiki_wiki.page(institution_name) 
    if not page.exists(): 
        return f"Page for {institution_name} not found on Wikipedia." 
    details = {} 
    details["Founder"] = get_wiki_info(page, 'founder') 
    details["Founded"] = get_wiki_info(page, 'founded') 
    details["Branches"] = get_wiki_info(page, 'branches') 
    details["Employees"] = get_wiki_info(page, 'employees') 
    details["Summary"] = page.summary[:300] 
    return details 
def get_wiki_info(page, keyword): 
    text = page.text.lower() 
    if keyword in text: 
        start_index = text.find(keyword) 
        end_index = text.find("\n", start_index) 
        return page.text[start_index:end_index].strip() 
    return "Not found" 
def main(): 
    institution = InstitutionInput(institution_name="IIT Madras") 
    result = fetch_institution_details(institution.institution_name) 
    if isinstance(result, dict): 
        print(f"Details of {institution.institution_name}:\n") 
        print(f"Founder: {result['Founder']}") 
        print(f"Founded: {result['Founded']}") 
        print(f"Branches: {result['Branches']}") 
        print(f"Employees: {result['Employees']}") 
        print(f"Summary: {result['Summary']}\n") 
    else: 
        print(result) 
if __name__ == "__main__": 
    main()