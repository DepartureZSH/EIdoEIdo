import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/home'
import IELTSForm from '@/components/IELTSForm'
import Listening from '@/components/Listening'
import Speaking from '@/components/Speaking'
import Vocabulary from '@/components/Vocabulary'
import Dictation from '@/components/Listening/Dictation'
import MyCorpus from '@/components/Listening/MyCorpus'
import Mock_exam from '@/components/Speaking/Mock_exam'
import Mock_part1 from '@/components/Speaking/Mock_part1'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [{
        path: '/',
        name: 'home',
        component: Home
    }, {
        path: '/Listening',
        name: 'Listening',
        component: Listening,
        children: [{
            path: '',
            name: 'Dictation',
            component: Dictation,
        }, {
            path: 'Dictation',
            name: 'Dictation',
            component: Dictation,
        }, {
            path: 'Corpus',
            name: 'MyCorpus',
            component: MyCorpus,
        }]
    }, {
        path: '/Speaking',
        name: 'Speaking',
        component: Speaking,
        children: [{
            path: '',
            name: 'Mock_exam',
            component: Mock_exam,
        }, {
            path: 'Mock_exam',
            name: 'Mock_exam',
            component: Mock_exam,
        }, {
            path: 'Mock_Part1',
            name: 'Mock_Part1',
            component: Mock_part1,
        }]
    }, {
        path: '/Vocabulary',
        name: 'Vocabulary',
        component: Vocabulary
    }]
})