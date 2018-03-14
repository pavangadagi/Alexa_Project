from flask import Flask
from flask_ask import Ask,statement,question

app = Flask(__name__)
ask = Ask(app,"/")

@ask.launch
def start():
    msg = 'hello....How can i help you?'
    return question(msg)



@ask.intent("Postmarriageintent")
def postmarriage(problem,p_affair,p_healthissues,p_children,p_longdistance):
    #SUBSTANCE ABUSE
    if problem == 'drugs' :
        return statement("Express your feelings, how his or her addiction issue has affected you negatively, and how it may be harming others, and even themselves. Avoid criticizing their actions directly, but instead, show them how their actions have caused harm.")
    elif problem == 'smoking':
        return statement("Try to talk to your partner and tell him the consequences of smoking. Tel him to take quitting as an incentive program rather than an inventory of unsatisfied cravings. You could also consider proposing e-cigarettes or nicotine gum. Be supportive and encourage him/her to develop positive attitude towards health. ")    
    elif problem == 'drinking' or problem == 'drunk':
        return statement("Sit with your partner and try to speak about his or her addiction.Self-help meetings and support groups like Alcoholics Anonymous or Narcotic Anonymous. So, if you have addiction problems, it is worth it to enter treatment, not only for you, but also for your partner, children, friends, and others")
    elif problem == 'porn':
        return statement("Try to talk to your partner about it. Be clear about how you feel, don’t hold back, be bold and say how you feel and try to create a positive conversation together. It is important to listen carefully to what your partner is telling you too. ")
    elif problem == 'gambling':
        return statement("Try to talk to your partner about his addiction issue and how it will affect your family and may lead to financial crisis. Support your husband if he is making a positive effort.Support groups such as Gamblers Anonymous might also point him or her in the right direction. Here is the Gamblers anonymous helpline. 8826904945.")
    
    #affair
    elif p_affair == 'cheating':
        return statement("	We all experience betrayal in different ways. The best thing to do is to acknowledge how you are feeling and not suppress it.Find an outlet for these emotions. It’s OK to cry and scream – it’s part of your healing process..Try to talk to your partner, ask him/her the reasons, remind him/her about your beautiful memories together. Revenge is not the best medicine.Especially if there are children involved, I would always advise,do the right things.•	Betrayal can be very humiliating, especially if other people knew about the affair. Remember you are not the person in the wrong here and however embarrassed or silly you may feel, it was not your fault. ")

    
    #health issues
    elif p_healthissues =='cancer' or p_healthissues =='lung disease' or p_healthissues =='disease' or p_healthissues == 'ill' or p_healthissues =='not well':
        return statement("Understand that it's not their fault. Understand that the illness has tainted their perception, so don't let their emotions dictate yours.Be supportive. Encourage your spouse to talk about his or her feelings. Due to illness, your spouse may not have the best self-insight. However, if the two of you can learn to communicate during the difficult times and express your emotions, you can each find a bit of peace.You need to seek medical help on your spouse's behalf. Prepare yourself to hold them accountable to take their medication and manage their illness.Together, you can work through this issue and become stronger,both individually AND as a union..")
    elif p_healthissues =='mental illness' or p_healthissues =='mentally disturbed' or p_healthissues =='bipolar disorder' or p_healthissues =='schizophrenia' :
        return statement("Understand that it's not their fault. Understand that the illness has tainted their perception, so don't let their emotions dictate yours.This will be hard to remember when having a spouse with mental illness, especially when your spouse takes his or her feelings and behavior out on you. But remind yourself that the mood and behaviour are symptoms of the illness. It's NOT personal. At the same time, set your boundaries and gently let your spouse know when they've crossed the line and hurt your feelings. Be supportive.Encourage your spouse to talk about his or her feelings.•	You need to seek medical help on your spouse's behalf. Prepare yourself to hold them accountable to take their medication and manage their illness. Together, you can work through this issue and become stronger — both individually AND as a union ")
    elif p_healthissues == 'handicapped' or p_healthissues =='physically disabled' or p_healthissues =='brain injuries' or p_healthissues =='physical injuries':
        return statement("Take care of your partner. Be supportive. Maybe look into support groups or counselling for your partner, as well as for yourself. It's to be expected, I think, that your relationship with your partner is in a rough spot, but that doesn't mean it won't get better. He/she will get better, either by recovering some of the functioning she’s/he's lost or by learning to live more fully in his/her new circumstances. As that happens, life will become a good deal, less hellish for you and you'll start to rebuild your lives and your marriage. ")
    
    #lack of responsibilty towards children
    elif p_children == 'children' or p_children == 'child' or p_children =='son' or p_children =='daughter':
        return statement("God has given the parents a very special and unique role in the family and children are Gods greatest blessing. Children seek love and care from their parents. So convince your husband to devote some time towards children after his busy schedule which will develop better understanding between them. ")
    
    #Long distance relationship
    elif p_longdistance == 'missing' or p_longdistance =='long distance relationship' or p_longdistance =='communication problem':
        return statement("The truth is, no couple can be in a long distance relationship for forever. Eventually we all need to settle down. It’s helpful to know when the other person is busy and when he or she is free, so that you can drop a text or make a call at the right time. This is especially essential when the both of you are living in different time zones. Greet each other good morning and good night every day this is a must. On top of that, try to update your partner on your life and its happenings. Be open and honest with each otherTo up the game, send each other pictures, audio clips and short videos from time to time. By putting in this kind of effort, you make the other person feel loved and attended to.")
    else:
        return statement("Sorry. I did not understand you")
    raise Exception()
        


if __name__ == ('__main__'):
    app.run(debug = True)
