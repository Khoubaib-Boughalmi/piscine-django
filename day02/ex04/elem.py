#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    class Text(str):
        def __str__(self):
            return super().__str__().replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace('\n', '\n<br />\n')


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """

    class ValidationError(Exception):
        def __init__(self) -> None:
            super().__init__("Validation Error.")

    def __init__(self, tag="div", attr={}, content=None, tag_type="double"):
        """
        __init__() method.

        Obviously.
        """

        self.tag = tag
        self.attr = attr
        self.content = []
        self.tag_type = tag_type
        if (not self.check_type(content) or content is None):
            raise Elem.ValidationError()
        if tag_type != "simple" and tag_type != "double":
            raise Elem.ValidationError()
        if type(content) == list:
            self.content = content
        elif type(content != None):
            self.content.append(content)

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        result = f'<{self.tag}{self.__make_attr()}'
        if self.tag_type == 'double':
            result += '>' + self.__make_content()
            result += f'</{self.tag}>'

        elif self.tag_type == 'simple':
            result += f'/>'
        return result
    
    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ""
        for pair in sorted(self.attr.items()):
            result += " " + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if len(self.content) == 0:
            return ""
        result = "\n"
        for elem in self.content:
            result += elem
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError()
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text("")]
        elif content != Text(""):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (
            isinstance(content, Elem)
            or type(content) == Text
            or (
                type(content) == list
                and all(
                    [type(elem) == Text or isinstance(elem, Elem) for elem in content]
                )
            )
        )


def test():
    html = Elem(
        "html",
        content=[
            Elem("head", content=Elem("title", content=Text('"Hello ground!"'))),
            Elem(
                "body",
                content=[
                    Elem("h1", content=Text('"Oh no, not again!"')),
                    Elem(
                        "img",
                        {"src": "http://i.imgur.com/pfp3T.jpg"},
                        tag_type="simple",
                    ),
                ],
            ),
        ],
    )
    print(html)


if __name__ == "__main__":
    [test()]
