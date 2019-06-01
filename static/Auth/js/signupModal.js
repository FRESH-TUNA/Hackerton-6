var signupModalComponent = {
    data: function(){
        return {
            csrfToken: Cookies.get('csrftoken'),
            modalState: true
        }
    },
    template:
    `
    <div id="signupModal" @click="onClickOutside" v-if="modalState">
        <div id="signupModalContent" @click.stop>
            <h1>Sign up!</h1>
            <form action="signup" method="POST">
                <input type="hidden" name="csrfmiddlewaretoken" :value="csrfToken">
                <label for="fname">e-mail</label>
                <input type="text" name="username" class="signupModalInput">
                <label for="fname">password</label>
                <input type="password" name="password1" class="signupModalInput">
                <label for="fname">repeat your password</label>
                <input type="password" name="password2" class="signupModalInput">
                <button type="submit">회원가입</button>
            </form>
        </div>
    </div>
    `,
    methods: {
        onClickOutside() {
            this.modalState = false;
        }
    }
}
var indexBox = new Vue({
    el: '#indexBox',
    methods: {
        onClickSignUp() {
            signup.state = 'sign-up-modal'
        }
    }
})

var signup = new Vue({
    el: '#signup',
    data: {
        state: null,
    },
    components: {
        'sign-up-modal': signupModalComponent,
    }
})