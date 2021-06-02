--
-- PostgreSQL database dump
--

-- Dumped from database version 12.6 (Ubuntu 12.6-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.6 (Ubuntu 12.6-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: appointment; Type: TABLE; Schema: public; Owner: erkan
--

CREATE TABLE public.appointment (
    appointment_id bigint NOT NULL,
    appointment_title character varying(255),
    appointment_detail text,
    appointment_date date,
    appointment_created timestamp without time zone,
    appointment_modified timestamp without time zone,
    appointment_status integer DEFAULT 0
);


ALTER TABLE public.appointment OWNER TO erkan;

--
-- Name: appointment_appointment_id_seq; Type: SEQUENCE; Schema: public; Owner: erkan
--

CREATE SEQUENCE public.appointment_appointment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.appointment_appointment_id_seq OWNER TO erkan;

--
-- Name: appointment_appointment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: erkan
--

ALTER SEQUENCE public.appointment_appointment_id_seq OWNED BY public.appointment.appointment_id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: erkan
--

CREATE TABLE public."user" (
    user_id bigint NOT NULL,
    user_fullname character varying(200),
    user_email character varying(150),
    user_password character varying(60),
    user_created timestamp without time zone,
    user_modified timestamp without time zone,
    user_status integer DEFAULT 1
);


ALTER TABLE public."user" OWNER TO erkan;

--
-- Name: user_user_id_seq; Type: SEQUENCE; Schema: public; Owner: erkan
--

CREATE SEQUENCE public.user_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_user_id_seq OWNER TO erkan;

--
-- Name: user_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: erkan
--

ALTER SEQUENCE public.user_user_id_seq OWNED BY public."user".user_id;


--
-- Name: appointment appointment_id; Type: DEFAULT; Schema: public; Owner: erkan
--

ALTER TABLE ONLY public.appointment ALTER COLUMN appointment_id SET DEFAULT nextval('public.appointment_appointment_id_seq'::regclass);


--
-- Name: user user_id; Type: DEFAULT; Schema: public; Owner: erkan
--

ALTER TABLE ONLY public."user" ALTER COLUMN user_id SET DEFAULT nextval('public.user_user_id_seq'::regclass);


--
-- Data for Name: appointment; Type: TABLE DATA; Schema: public; Owner: erkan
--

COPY public.appointment (appointment_id, appointment_title, appointment_detail, appointment_date, appointment_created, appointment_modified, appointment_status) FROM stdin;
8	test	testtt	2021-05-20	2021-05-05 22:32:02.550788	2021-05-05 23:05:05.077356	1
9	test 2	test	2021-05-13	2021-05-05 23:06:49.209453	2021-05-05 23:06:49.209455	1
10	test 3		2021-05-21	2021-05-05 23:07:15.591796	2021-05-05 23:07:15.591798	1
11	test 3333	dddd	2021-05-25	2021-05-05 23:07:29.775212	2021-05-05 23:07:29.775216	1
12	test yeni		2021-05-25	2021-05-05 23:07:56.338247	2021-05-05 23:07:56.33825	1
13	easd	ads	2021-05-26	2021-05-05 23:08:10.332626	2021-05-05 23:08:10.33263	1
14	test yeni randevu	asdasd	2021-05-26	2021-05-05 23:08:55.627527	2021-05-05 23:08:55.62753	1
15	test yeni rand	adasd	2021-05-17	2021-05-05 23:09:32.223793	2021-05-05 23:09:32.223795	1
16	tasdasd	adasd	2021-05-26	2021-05-05 23:10:21.923138	2021-05-05 23:10:21.923141	1
17	test 77777		2021-05-26	2021-05-05 23:10:34.271533	2021-05-05 23:10:34.271538	1
18	yeni randevu	asdasd	2021-05-17	2021-05-05 23:10:53.900101	2021-05-05 23:10:53.900104	1
19	test randevusu 1		2021-05-27	2021-05-05 23:11:11.503417	2021-05-05 23:11:11.503419	1
20	test randevusu 1 1		2021-05-20	2021-05-05 23:11:18.231537	2021-05-05 23:11:18.231539	1
21	test randevusu 1111 		2021-05-18	2021-05-05 23:11:25.599427	2021-05-05 23:11:25.59943	1
22	test randevusu 22		2021-05-24	2021-05-05 23:11:34.320104	2021-05-05 23:11:34.320106	1
23	test randevusu 1234		2021-05-19	2021-05-05 23:11:42.268314	2021-05-05 23:11:42.268317	1
24	bugün	test	2021-05-06	2021-05-06 00:11:59.432987	2021-06-03 00:28:50.873016	0
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: erkan
--

COPY public."user" (user_id, user_fullname, user_email, user_password, user_created, user_modified, user_status) FROM stdin;
2	Erkan Keskin	keskin.erkan@gmail.com	123123*	2021-05-05 21:17:08	2021-05-05 21:17:08	1
\.


--
-- Name: appointment_appointment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: erkan
--

SELECT pg_catalog.setval('public.appointment_appointment_id_seq', 24, true);


--
-- Name: user_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: erkan
--

SELECT pg_catalog.setval('public.user_user_id_seq', 2, true);


--
-- Name: appointment appointment_pk; Type: CONSTRAINT; Schema: public; Owner: erkan
--

ALTER TABLE ONLY public.appointment
    ADD CONSTRAINT appointment_pk PRIMARY KEY (appointment_id);


--
-- Name: user user_pk; Type: CONSTRAINT; Schema: public; Owner: erkan
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pk PRIMARY KEY (user_id);


--
-- PostgreSQL database dump complete
--

