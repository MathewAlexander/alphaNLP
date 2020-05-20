from django.shortcuts import render,redirect
from django.utils import timezone

from .forms import QAForm
from ip2geotools.databases.noncommercial import DbIpCity
import torch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
tokenizer = AutoTokenizer.from_pretrained("elgeish/cs224n-squad2.0-albert-base-v2")
model = AutoModelForQuestionAnswering.from_pretrained("elgeish/cs224n-squad2.0-albert-base-v2")
#
def predict_answer_QA(question, text):
    input_dict = tokenizer.encode_plus(question, text, return_tensors='pt', max_length=512)
    input_ids = input_dict["input_ids"].tolist()
    start_scores, end_scores = model(**input_dict)

    start = torch.argmax(start_scores)
    end = torch.argmax(end_scores)

    all_tokens = tokenizer.convert_ids_to_tokens(input_ids[0])
    answer = ''.join(all_tokens[start: end + 1]).replace('▁', ' ').strip()
    answer = answer.replace('[SEP]', '')
    return answer if answer != '[CLS]' and len(answer) != 0 else 'could not find an answer'

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
#
#
# def demo_qa(request):
#     text="The goal of this model is to save CS224n students GPU time when establising baselines to beat for the Default Final Project. The training set used to fine-tune this model is the same as the official one; however, evaluation and model selection were performed using roughly half of the official dev set, 6078 examples, picked at random. The data files can be found at https://github.com/elgeish/squad/tree/master/data — this is the Winter 2020 version. Given that the official SQuAD2.0 dev set contains the project's test set, students must make sure not to use the official SQuAD2.0 dev set in any way — including the use of models fine-tuned on the official SQuAD2.0, since they used the official SQuAD2.0 dev set for model selection."
#     question="What is the goal of this?"
#     answer_text=answer(question, text)
#     print("!!!!!!",answer_text )
#     context = {
#         'answer_text': answer_text
#     }
#
#     return render(request, 'qa.html', context)


def qa_inference(request):
    if request.method == "POST":
        form = QAForm(request.POST)
        if form.is_valid():
            ip = get_client_ip(request)
            data = DbIpCity.get(str(ip), api_key='free')
            user = str(data.to_json())

            # user='test user'
            post = form.save(commit=False)
            post.user = user
            post.published_date = timezone.now()

            para = post.context
            question = post.question
            result = predict_answer_QA(question,para)
            post.answer = result

            post.save()

            start = para.lower().find(result)
            end = start + len(result)
            para1 = para[:start]
            para2 = para[end:]



            return render(request,'qa_result.html', {'para1':para1,'para2':para2,'result':result})
    else:
        form = QAForm()
    return render(request, 'qaForm.html', {'form': form})


def demo_index(request):

    return render(request, 'demo_index.html')



