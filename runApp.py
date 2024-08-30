from flask import Flask, request,render_template
from pytube import YouTube
import speech_recognition as sr
import  os


app = Flask(__name__)



def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')

