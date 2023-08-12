from sqlalchemy import select

from database_models import Prompts, Models, Experiments


############ experiments #######################

def add_prompt(session, short_name, prompt_text):
    new_item = Prompts(short_name=short_name,
                       prompt_text=prompt_text)
    session.add(new_item)
    session.commit()
    new_id = new_item.id
    return new_id


def get_prompt(session, short_name) -> Prompts:
    query_result = session.execute(select(Prompts).filter(Prompts.short_name == short_name)).first()

    if query_result is not None:
        return query_result.Prompts


def get_prompt_names(session) -> Prompts:
    query_result = session.execute(select(Prompts.short_name)).all()

    if query_result is not None:
        return [x[0] for x in query_result]


def add_model(session, model_name):
    new_item = Models(model_name=model_name)
    session.add(new_item)
    session.commit()
    new_id = new_item.id
    return new_id


def get_model(session, model_name) -> Models:
    query_result = session.execute(select(Models).filter(Models.model_name == model_name)).first()

    if query_result is not None:
        return query_result.Models


def add_experiment(session, model_id, prompt_id, message_set, results):
    new_item = Experiments(model_id=model_id,
                           prompt_id=prompt_id,
                           message_set=message_set,
                           results=results)
    session.add(new_item)
    session.commit()
    new_id = new_item.id
    return new_id


def get_experiment(session, model_id, prompt_id, message_set='bmks_81'):
    query_result = session.execute(select(Experiments) \
                                   .filter(Experiments.model_id == model_id) \
                                   .filter(Experiments.prompt_id == prompt_id) \
                                   .filter(Experiments.message_set == message_set)).first()

    if query_result is not None:
        return query_result.Experiments
