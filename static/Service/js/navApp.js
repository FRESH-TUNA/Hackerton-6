var nav = {
    template:
    `
    <nav class="navbar navbar-expand-lg navbar-light">
        <a class="navbar-brand" @click="showReadPostsComponent">{{title}}</a>
        <button type="button" class="btn btn-primary" @click="showCreatePostComponent" v-show="loginState">New Document</button>
        <button type="button" class="btn btn-primary" @click="signout" v-show="loginState">Sign out</button>
        <button type="button" class="btn btn-primary" @click="showSignInModal" v-show="!loginState">Sign in</button>
        <button type="button" class="btn btn-primary" @click="showSignupModal">Sign up</button>

        <component
            :is="modalComponentState"
            @on-click-outside="modalComponentState = false"
            
            @after-create-account="modalComponentState = false"
            @after-login-success="showUserInfo"
        ></component>
        <a class="navbar-brand" v-if="loginState">welcome {{username}}</a>
    </nav>
    `,
    data: {
        return {
            title: 'TunaBoard',
            modalComponentState: null,
            loginState: false,
            username: ''
        }  
    }
}
