BEGIN;


CREATE TABLE IF NOT EXISTS public.slot
(
    id serial NOT NULL,
    code character varying(12) NOT NULL UNIQUE,
    number smallint NOT NULL,
    floor character varying(1) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.car
(
    id serial NOT NULL,
    code character varying(125) NOT NULL UNIQUE,
    lic_plate character(7) NOT NULL,
    brand character varying(50) NOT NULL,
    model character varying(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.occupation
(
    id serial NOT NULL,
    slot_id smallint NOT NULL,
    car_id smallint,
    user_id smallint NOT NULL,
    entry time with time zone,
    exit time with time zone
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

ALTER TABLE IF EXISTS public.occupation
    ADD CONSTRAINT fk_occupation_slot FOREIGN KEY (slot_id)
    REFERENCES public.slot (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.occupation
    ADD CONSTRAINT fk_occupation_car FOREIGN KEY (car_id)
    REFERENCES public.car (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.occupation
    ADD CONSTRAINT fk_occupation_user FOREIGN KEY (user_id)
    REFERENCES public.user (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

END;