from flask import Flask, render_template, request
import os
app = Flask(__name__)
fig_folder=os.path.join('static','figs')
app.config['UPLOAD_FOLDER'] = fig_folder

analysis_type=["Distripution of students numbers in every study field", "Number of bus students relative to years",
"Number of english students relative to years- All","Number of IT students relative to years- All","Number of media students relative to years- All",
"Number of graphic students relative to years- All","Number of students for all study fields relative to years -Genderdized",
"Number of bus students relative to secondary school","Number of english students relative to secondary school",
"Number of IT students relative to secondary school","Number of media students relative to secondary school",
"Number of graphic students relative to secondary school","Number of bus students relative to both year & secondary school",
"Number of english students relative to both year & secondary school","Number of IT students relative to both year & secondary school",
"Number of media students relative to both year & secondary school","Number of graphic students relative to both year & secondary school"
]
@app.route("/")
def home():
    return render_template ('index.html')

@app.route("/results", methods=["POST"])
def results():
    global analysis_type
    analyse= '%s' %(request.form['analysis_wanted'])
    if analyse == analysis_type[0]:
        fig='figure1.png'
        result="""
        As observed from the two plots done above there is many points that is needed to be mentioned:
        1.The absence of students in the graphic_students has the lion share relative to the other range of numbers in all of students fields // 

        2.Both graphics and english students numbers has a high concentration in a small range of numbers.(For graphics student, it is because of the little number of students in this field compared to other fields. But for English students it seems like the number of students is nearly fixed in the range between (0 &50) over years for all secondary school) // 

        3.Most of the number ranges for all of the study fields for students lies between: zero and nearly 75 // 

        4.There is gaps in ranges of numbers for each students’ field"""
    elif analyse == analysis_type[1]:
        fig='figure2.png'
        result="""Bus students have a density in their numbers in nearly years 2016-2017 but obviously the number of bus students is extremely larger compared to english students"""
    elif analyse == analysis_type[2]:
        fig='figure3.png'
        result = '''English students has a density in their numbers in nearly years 2016-2017 but obviously the number of bus students is extremely larger compared to english students'''
    elif analyse == analysis_type[3]:
        fig='figure4.png'
        result= '''IT students has denisty area in their students numbers in nearly years 2015-2016'''
    elif analyse == analysis_type[4]:
        fig='figure5.png'
        result='''media students has density area in -nearly- year 2011 or 2012 because of zeros that omit the null values that is huge compared to the number of students in those fields which is a small number over the 7 or the 8 years that are recorded in their tables (df4 & df6) compared to the recorded numbers for the students in the other study fields'''
    elif analyse == analysis_type[5]:
        fig='figure6.png'
        result = '''Graphic students has there density area in -nearly- year 2011 or 2012 because of zeros that omit the null values that is huge compared to the number of tsudents in those fields which is a small number over the 7 or the 8 years that are recorded in their tables (df4 & df6) compared to the recorded numbers for the students in the other study fields'''
    elif analyse == analysis_type[6]:
        fig='figure7.png'
        result= '''As it is seen from the pairplot above: ///

1.For bus students, the number of students shows instability as it goes decreases going to 2012 then increses going to 2012 and goes on the same way every 2 years. /// 

1.1 over all of the years there is a gap that increases between the number of males and females for the favor of males, in which number of female students do not exceed 10,000 students/year over the 10 years while males go beyond that. /// 

1.2 The year 2014 scores the most number of students/year for both males and females. /// 

1.3 the heighst number of students over all fields of study is shown in the bus field. /// 

2.The english_students goes in the opposite direction for all of the students in other fields, as the number of female students is larger than number of male students/ year & over years & the gap between them increases over years 2.1 The number of male students shows a small increase over years and is nearly constant from the year 2014 till now. /// 

2.2the females numbers have instability whether for increasing and decreasing over years, but generally the numbers has a tendency twords increasing for females. /// 

3.The number of female IT students is nearly constant over years with a small percentage of increase compared to the males which shows a high increase over the years except for the years (2015-2016-2017) which shows a drawback in the number of male students but after that they tend to increase again. /// 

3.1 generally for IT department, number of male students is much larger than the number of female students. /// 

3.2 The heighst number of males in a field of study is in the IT. /// 

For both media & graphic section we will have to ignore the first three years. /// 

4 for media students, the numbers of males and females are so near over the years for the favor of males and there is a general tendency to increase for both. /// 

5.1 For graphics students, there is a tendency for female students to increase over time. /// 

5.2 the gap between the number of males and females is the largest in the year 2016. /// 

5.3 There is no females in year 2018. /// 

5.4 this point is the most amazing fact in the previous plot, as the number of females -after disappering in the year 2018- in the year 2019 is more than the number of males and it scores the most number of females/year. /// 

Generally, the number of males is more distributed on the graph over the years than the females, that has density representing most of their numbers in a certain two or 3 years. /// 

This general observation for students numbers in different fields may show a tendency for women to go in studying the literatural subjects than scientific subjects'''
    elif analyse == analysis_type[7]:
        fig='figure8.png'
        result= '''The number of students that came from different secondary schools (59 schools) in bus field is constant/study field.'''
    elif analyse == analysis_type[8]:
        fig='figure9.png'
        result= '''The number of students that came from different secondary schools (59 schools) in english field is constant/study field.'''
    elif analyse == analysis_type[9]:
        fig='figure10.png'
        result= '''The number of students that came from different secondary schools (59 schools) in IT field is constant/study field.'''
    elif analyse == analysis_type[10]:
        fig='figure11.png'
        result= '''The number of students that came from different secondary schools (59 schools) in media field is constant/study field.'''
    elif analyse == analysis_type[11]:
        fig='figure12.png'
        result= '''The number of students that came from different secondary schools (59 schools) in graphic field is constant/study field.'''
    elif analyse == analysis_type[12]:
        fig='figure13.png'
        result ='''As it is obvious from the pivot_table above that is plotted by heatmap, The number of students for bus field from a specific secondary school is fixed/year.'''
    elif analyse == analysis_type[13]:
        fig='figure14.png'
        result ='''As it is obvious from the pivot_table above that is plotted by heatmap, The number of students for english field from a specific secondary school is fixed/year.'''
    elif analyse == analysis_type[14]:
        fig='figure15.png'
        result ='''As it is obvious from the pivot_table above that is plotted by heatmap, The number of students for IT field from a specific secondary school is fixed/year.'''
    elif analyse == analysis_type[15]:
        fig='figure16.png'
        result ='''As it is obvious from the pivot_table above that is plotted by heatmap, The number of students for media field from a specific secondary school is fixed/year.'''
    elif analyse == analysis_type[16]:
        fig='figure17.png'
        result ='''As it is obvious from the pivot_table above that is plotted by heatmap, The number of students for graphic field from a specific secondary school is fixed/year.'''
    else:
        fig= 'null-value.jpg'
        result= " Please choose some option to show results "
    figure = os.path.join(app.config['UPLOAD_FOLDER'], fig)
    return render_template("index.html", user_image = figure, result= result)

if __name__ == "__main__":
    app.run()