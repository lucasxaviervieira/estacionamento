BEGIN;


CREATE TABLE IF NOT EXISTS public.vaga
(
    id serial NOT NULL,
    codigo character varying(12) NOT NULL,
    numero smallint NOT NULL,
    andar character varying(1) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.carro
(
    id serial NOT NULL,
    codigo character varying(125) NOT NULL,
    placa character(7) NOT NULL,
    marca character varying(50) NOT NULL,
    modelo character varying(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.ocupacao
(
    id serial NOT NULL,
    vaga_id smallint NOT NULL,
    carro_id smallint,
    user_id smallint NOT NULL,
    entrada time with time zone,
    saida time with time zone
);

CREATE TABLE IF NOT EXISTS public.user
(
    id serial NOT NULL,
    name character varying(125) NOT NULL,
    username character varying(125) NOT NULL,
    password character varying(255) NOT NULL,
    role character varying(6) NOT NULL DEFAULT 'normal',
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.ocupacao
    ADD CONSTRAINT fk_ocupacao_vaga FOREIGN KEY (vaga_id)
    REFERENCES public.vaga (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.ocupacao
    ADD CONSTRAINT fk_ocupacao_carro FOREIGN KEY (carro_id)
    REFERENCES public.carro (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.ocupacao
    ADD CONSTRAINT fk_ocupacao_user FOREIGN KEY (user_id)
    REFERENCES public.user (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

END;