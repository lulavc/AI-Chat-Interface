from flask import Flask, render_template, request, jsonify
import os
import ollama

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        prompt = data.get('prompt')
        mode = data.get('mode', 'direct')
        model = data.get('model', 'mistral-chat')
        language = data.get('language', 'en')

        if not prompt:
            return jsonify({'error': 'Prompt não fornecido'})

        if mode == 'agents':
            # Multi-agent system logic
            response = process_multi_agent(prompt)
        else:
            # Direct chat logic
            response = process_direct_chat(prompt, model, language)

        return jsonify({'response': response})

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/clear_history', methods=['POST'])
def clear_history():
    try:
        data = request.json
        mode = data.get('mode', 'direct')
        # Clear chat history logic here
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/get_agent_prompts', methods=['GET'])
def get_agent_prompts():
    try:
        # Get agent prompts logic here
        return jsonify({'response': 'Agent prompts retrieved successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

def process_multi_agent(prompt):
    # Implement multi-agent system logic here
    agents = ['CEO', 'Analista', 'Coder', 'Analista', 'CEO']
    response = ""
    
    for agent in agents:
        response += f"### {agent}\n"
        response += ollama.chat(model='mistral-chat', messages=[{
            'role': 'user',
            'content': f"Você é o {agent}. Responda: {prompt}"
        }])['message']['content']
        response += "\n\n"
    
    return response

def process_direct_chat(prompt, model, language):
    # Implement direct chat logic here
    return ollama.chat(model=model, messages=[{
        'role': 'user',
        'content': prompt
    }])['message']['content']

def main():
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=True)

if __name__ == '__main__':
    main()
