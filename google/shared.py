from fastui import AnyComponent, components as c


def layout(
    *components: list[AnyComponent],
    title: str = 'Google',
    class_name: str = 'container',
) -> list[AnyComponent]:
    return [
        c.PageTitle(text=title),
        c.Page(
            components=components,
            class_name=class_name,
        ),
    ]
