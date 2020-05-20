from django.shortcuts import render
from demos.models import Demo
import torch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
tokenizer = AutoTokenizer.from_pretrained("elgeish/cs224n-squad2.0-albert-base-v2")
model = AutoModelForQuestionAnswering.from_pretrained("elgeish/cs224n-squad2.0-albert-base-v2")

def answer(question, text):
    input_dict = tokenizer.encode_plus(question, text, return_tensors='pt', max_length=512)
    input_ids = input_dict["input_ids"].tolist()
    start_scores, end_scores = model(**input_dict)

    start = torch.argmax(start_scores)
    end = torch.argmax(end_scores)

    all_tokens = tokenizer.convert_ids_to_tokens(input_ids[0])
    answer = ''.join(all_tokens[start: end + 1]).replace('▁', ' ').strip()
    answer = answer.replace('[SEP]', '')
    return answer if answer != '[CLS]' and len(answer) != 0 else 'could not find an answer'


def demo_qa(request):
    text="The goal of this model is to save CS224n students GPU time when establising baselines to beat for the Default Final Project. The training set used to fine-tune this model is the same as the official one; however, evaluation and model selection were performed using roughly half of the official dev set, 6078 examples, picked at random. The data files can be found at https://github.com/elgeish/squad/tree/master/data — this is the Winter 2020 version. Given that the official SQuAD2.0 dev set contains the project's test set, students must make sure not to use the official SQuAD2.0 dev set in any way — including the use of models fine-tuned on the official SQuAD2.0, since they used the official SQuAD2.0 dev set for model selection."
    question="What is the goal of this?"
    answer_text=answer(question, text)
    print("!!!!!!",answer_text )
    context = {
        'answer_text': answer_text
    }

    return render(request, 'qa.html', context)

def demo_index(request):
    demos = Demo.objects.all()
    context = {
        'demos': demos
    }
    return render(request, 'demo_index.html', context)


def demo_detail(request, pk):
    demo = Demo.objects.get(pk=pk)
    context = {
        'demo': demo
    }
    return render(request, 'demo_detail.html', context)
