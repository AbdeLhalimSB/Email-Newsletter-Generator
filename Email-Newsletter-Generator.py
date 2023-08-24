from faker import Faker

# Create a Faker instance
fake = Faker()

def generate_medium_paragraph(sentences_count=3, sentence_length=10):
    paragraph = [fake.sentence(nb_words=sentence_length) for _ in range(sentences_count)]
    return " ".join(paragraph)


if __name__ == "__main__":
    html = f'''
<!DOCTYPE html>
<html lang="en">
<center>
    <body>
        <h1 style="color: gold;" >{generate_medium_paragraph(sentences_count=1, sentence_length=6)}</h1>
        <br><hr><br>
        <p>{generate_medium_paragraph(sentences_count=1, sentence_length=50)}</p>
        <img src="https://picsum.photos/500/500" alt="Image">
        <p>{generate_medium_paragraph(sentences_count=1, sentence_length=50)}</p>
        <p>{generate_medium_paragraph(sentences_count=1, sentence_length=50)}</p>
        <br><hr><br>
        <div>
            <h6>If you no longer wish to receive our new emails, please <span style="text-decoration: underline;">unsubscribe</span> from our mailing list.</h6>
        </div>
    </body>
</center>
<style>
    body'''+'{'+'''
        color: black;
        font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    }
    p'''+'{'+'''
        color: black;
    }
</style>
</html>
    '''
    file = open('output.html','w')
    file.writelines(html)
    file.close()