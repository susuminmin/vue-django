import Vue from 'vue'
import Vuex from 'vuex'
import jwtDecode from 'jwt-decode'

Vue.use(Vuex)

export default new Vuex.Store({
  // 상태
  state: {
    token: null,
  },
  // computed
  getters: {
    isLoggedIn(state) {
      return state.token ? true : false
    },
    options(state) {
      return {
        headers: {
          Authorization: 'JWT ' + state.token
        }
      }
    },
    userId(state) {
      return state.token ? jwtDecode(state.token).user_id : null // token 유무 따른 다른 값 리턴
    },
  },
  // 상태 변경 함수 
  mutations: {
    setToken(state, token) {
      state.token = token  // 전달받은 token 값으로 바꾸겠다. 
    }
  },
  // method
  actions: {
    logIn(context, token) {
      context.commit('setToken', token)
    },
    logOut(context) {
      context.commit('setToken', null) // 로그아웃 null로 변경
    }
  },
})
