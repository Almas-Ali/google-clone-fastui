from fastapi.routing import APIRouter

from fastui import FastUI, AnyComponent, components as c
from fastui.events import GoToEvent

from pydantic import BaseModel

from googlesearch import Search as Google
from googlesearch.models import SearchResultElement

from google.shared import layout

router = APIRouter()


class Search(BaseModel):
    q: str


@router.get('/api/', response_model=FastUI, response_model_exclude_none=True)
def home() -> AnyComponent:
    return layout(
        c.Div(
            components=[
                c.Image(
                    src='https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
                    alt='Google Logo',
                    width=272,
                    height=92,
                ),
            ],
            class_name='text-center',
        ),
        c.Div(
            components=[
                c.ModelForm[Search](
                    submit_url='/search',
                    initial={},
                    method='GOTO',
                    submit_on_change=True,
                    display_mode='inline',
                    class_name='my-4 w-75 rounded-pill mx-auto',
                ),
            ],
            class_name='text-center',
        ),
        c.Div(
            components=[
                c.Button(
                    text='Google Search',
                    class_name='text-sm btn btn-secondary mx-2',
                ),
                c.Button(
                    text="I'm Feeling Lucky",
                    class_name='text-sm btn btn-secondary mx-2',
                ),
            ],
            class_name='my-4 text-center',
        ),
        c.Div(
            components=[
                c.Paragraph(
                    text='Google offered in:',
                    class_name='text-sm',
                ),
                c.LinkList(
                    links=[
                        c.Link(
                            components=[c.Text(text='English')],
                            on_click=GoToEvent(url='/'),
                            class_name='mx-2',
                        ),
                        c.Link(
                            components=[c.Text(text='हिन्दी')],
                            on_click=GoToEvent(url='/'),
                            class_name='mx-2',
                        ),
                        c.Link(
                            components=[c.Text(text='বাংলা')],
                            on_click=GoToEvent(url='/'),
                            class_name='mx-2',
                        ),
                    ],
                    class_name='text-sm',
                ),
            ],
            class_name='my-4 text-center',
        ),
    )


@router.get('/api/search', response_model=FastUI, response_model_exclude_none=True)
def search_page(
    q: str,
    page: int = 1,
) -> AnyComponent:
    page_size = 10
    _results = results(q)
    results_data = _results[(page - 1) * page_size : page * page_size]

    return layout(
        c.Div(
            components=[
                c.Div(
                    components=[
                        c.Link(
                            components=[
                                c.Image(
                                    src='https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_92x30dp.png',
                                    alt='Google Logo',
                                    width=92,
                                    height=30,
                                ),
                            ],
                            on_click=GoToEvent(url='/'),
                            class_name='mx-2',
                        ),
                    ],
                    class_name='col-4 col-sm-3 col-md-2 col-lg-1',
                ),
                c.Div(
                    components=[
                        c.ModelForm[Search](
                            submit_url='/search',
                            initial={},
                            method='GOTO',
                            submit_on_change=True,
                            display_mode='inline',
                            class_name='mx-2 w-100 rounded-pill',
                        ),
                    ],
                    class_name='col-8 col-sm-8 col-md-8 col-lg-8',
                ),
                c.Div(
                    components=[
                        c.Div(
                            components=[
                                c.Div(
                                    components=[
                                        c.Link(
                                            components=[
                                                c.Paragraph(
                                                    text=result.title,
                                                    class_name='fs-5 icon-link icon-link-hover link-info link-underline-info link-underline-opacity-25',
                                                ),
                                            ],
                                            on_click=GoToEvent(url=result.url),
                                            class_name='icon-link icon-link-hover link-info link-underline-info link-underline-opacity-25',
                                        ),
                                        c.Paragraph(
                                            text=result.displayed_url,
                                            class_name='card-text text-muted fs-6',
                                        ),
                                        c.Paragraph(
                                            text=result.description,
                                            class_name='card-text',
                                        ),
                                    ],
                                    class_name='card-body',
                                ),
                            ],
                            class_name='card border-0 w-75',
                        )
                        for result in results_data
                    ],
                    class_name='ml-5',
                ),
                c.Pagination(
                    page=page,
                    page_size=page_size,
                    total=len(_results),
                    class_name='mx-auto',
                ),
            ],
            class_name='row g-3',
        ),
        title=f'{q} - Google Search',
        class_name='m-4',
    )


def results(query: str) -> list[SearchResultElement]:
    """Searches Google for the given query and returns the results."""
    _search = Google(
        query=query,
        number_of_results=100,
        language='en',
        retry_count=10,
    )

    for result in _search.results:
        result.displayed_url = result.displayed_url.replace(result.title, '')

    return _search.results
