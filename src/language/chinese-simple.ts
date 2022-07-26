import { Language } from './index'

const chineseSimple: Language = {
  errorMsg: 'Bot莫名其妙炸了，麻烦通知一下群主',
  coinBalanceDisplay (amount: number | string): string {
    return `金币：${amount}`
  },
  viewProfile: {
    profile: '档案',
    inXXX (guildName: string): string {
      return `在${guildName}`
    },
    yourExp: '你自己的'
  },
  commands: {
    getMyProfile: {
      name: 'profile',
      desc: '查看我的信息'
    }
  },
  mumble: {
    mumble: '骂ta',
    language (mumbleFrom: string, mumbleObject: string): string {
      const mubleArr = ['草泥马', '我去年买了个表', '你tm的', '你是不是傻']
      const ramdomNumber = Math.floor(Math.random() * mubleArr.length)
      return `${mumbleFrom}对${mumbleObject}说："${mubleArr[ramdomNumber]}"`
    }
  },
  setGuildProfile: {
    command: 'config',
    commandDesc: '设置你的Bot（仅限管理员）',
    title: '设置',
    announcementChannelOption: '公告频道',
    administratorRoleOption: '管理员tag',
    timeZoneOption: '时区',
    notificationChannelOption: '消息频道（用于通知）',
    languageOption: '语言'
  }
}

export default chineseSimple